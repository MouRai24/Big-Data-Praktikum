import argparse, yaml
from pathlib import Path

from src.weaklink.io import load_pair_data
from src.weaklink.preprocess import impute_and_cast
from src.weaklink.models import make_model
from src.weaklink.snorkel_utils import apply_lfs, combine_with_label_model, coverage
from src.weaklink.evaluation import eval_report
from src.weaklink.reporting_markdown import MDWriter
from src.weaklink.lfs.stats import make_average_lf, make_median_lf, make_variance_pick_lf, make_weighted_mean_lf, make_count_high_lf, make_low_all_lf, make_single_feature_lf
from src.weaklink.lfs.graph import make_graph_lf
from src.weaklink.tuning.dev import tune_lf_on_dev
from src.weaklink.tuning.kfold import cv_tune_lf

def build_lfs(kind_list, df_ref, feature_cols):
    """Create LF objects from a config list."""
    lfs = []
    var = df_ref[feature_cols].var()
    uniq = var / var.sum() if var.sum() else var
    for spec in kind_list:
        t = spec["type"].lower()
        if t == "average":
            lfs.append(make_average_lf(feature_cols, spec["high"], spec["low"]))
        elif t == "median":
            lfs.append(make_median_lf(feature_cols, spec["high"], spec["low"]))
        elif t == "variance":
            lfs.append(make_variance_pick_lf(feature_cols, var, spec["high"], spec["low"]))
        elif t == "weighted":
            lfs.append(make_weighted_mean_lf(feature_cols, uniq, spec["high"], spec["low"]))
        elif t == "count_high":
            lfs.append(make_count_high_lf(feature_cols, spec["value_thresh"], spec["min_count"], spec.get("max_count_nonmatch", 2)))
        elif t == "low_all":
            lfs.append(make_low_all_lf(feature_cols, spec["max_value"]))
        elif t == "single_feature":
            feat = spec["feature"]
            if feat not in feature_cols:
                raise ValueError(
                    f"single_feature '{feat}' not found. Available features include (first 20): {feature_cols[:20]}"
                )
            lfs.append(make_single_feature_lf(feat, spec["high"], spec["low"]))
        elif t == "graph":
            lfs.append(make_graph_lf(df_ref, spec["threshold"], spec.get("min_component_size",3)))
        else:
            raise ValueError(f"Unknown LF type: {t}")
    return lfs

def run_supervised(cfg):
    """Run a fully supervised baseline."""
    df_tr, df_te, feature_cols = load_pair_data(cfg["data"]["train"], cfg["data"]["test"], cfg["data"].get("exclude"))
    impute_and_cast(df_tr, feature_cols); impute_and_cast(df_te, feature_cols)
    X_tr, y_tr = df_tr[feature_cols].values, df_tr["label"].values
    X_te, y_te = df_te[feature_cols].values, df_te["label"].values
    mdl = make_model(cfg["model"]["name"], **cfg["model"].get("params", {}))
    mdl.fit(X_tr, y_tr)
    report = eval_report(y_te, mdl.predict(X_te))
    wr = MDWriter(cfg["output"]["md"])
    wr.title("Fully Supervised Evaluation")
    wr.section("Model Parameters")
    wr.bullets({k: str(v) for k,v in cfg["model"].get("params", {}).items()})
    wr.section("Classification Report")
    wr.codeblock(report); wr.save()

def run_weak(cfg):
    """Run a weak supervision pipeline with optional Snorkel combination."""
    df_tr, df_te, feature_cols = load_pair_data(cfg["data"]["train"], cfg["data"]["test"], cfg["data"].get("exclude"))
    impute_and_cast(df_tr, feature_cols); impute_and_cast(df_te, feature_cols)
    X_tr, X_te, y_te = df_tr[feature_cols].values, df_te[feature_cols].values, df_te["label"].values
    lfs = build_lfs(cfg["lfs"], df_tr, feature_cols)
    wr = MDWriter(cfg["output"]["md"])
    wr.title("Weak Supervision Evaluation")
    wr.section("LFs")
    wr.bullets({f"lf_{i}": lf.name for i,lf in enumerate(lfs,1)})

    if cfg.get("per_lf", True):
        for lf in lfs:
            from snorkel.labeling import PandasLFApplier
            L = PandasLFApplier([lf]).apply(df_tr).ravel()
            m = L != -1
            mdl = make_model(cfg["model"]["name"], **cfg["model"].get("params", {}))
            if m.sum() > 0:
                mdl.fit(X_tr[m], L[m])
                rep = eval_report(y_te, mdl.predict(X_te))
            else:
                rep = "No coverage."
            wr.section(lf.name)
            wr.line(f"Coverage: {coverage(L):.3%}")
            wr.codeblock(rep)

    if cfg.get("combine", True):
        from snorkel.labeling import PandasLFApplier
        L_all = PandasLFApplier(lfs).apply(df_tr)
        y_pseudo = combine_with_label_model(L_all, cardinality=2,
                                            n_epochs=cfg.get("label_model",{}).get("n_epochs",200),
                                            lr=cfg.get("label_model",{}).get("lr",0.01))
        mdl = make_model(cfg["model"]["name"], **cfg["model"].get("params", {}))
        mdl.fit(X_tr, y_pseudo)
        wr.section("Snorkel Combined")
        wr.line(f"Coverage: {coverage(y_pseudo):.3%}")
        wr.codeblock(eval_report(y_te, mdl.predict(X_te)))
    wr.save()

def run_tune_dev(cfg):
    """Run dev-set tuning for selected LFs."""
    from sklearn.model_selection import train_test_split
    df_tr, df_te, feature_cols = load_pair_data(cfg["data"]["train"], cfg["data"]["test"], cfg["data"].get("exclude"))
    impute_and_cast(df_tr, feature_cols); impute_and_cast(df_te, feature_cols)
    df_a, df_b = train_test_split(df_tr, test_size=cfg["tuning"].get("dev_size",0.1), random_state=42, stratify=df_tr["label"])
    results = {}
    for spec in cfg["tuning"]["lfs"]:
        t = spec["type"].lower()
        if t == "average":
            grid = spec["grid"]
            factory = lambda p: make_average_lf(feature_cols, p["high"], p["low"])
        elif t == "median":
            grid = spec["grid"]
            factory = lambda p: make_median_lf(feature_cols, p["high"], p["low"])
        elif t == "graph":
            grid = spec["grid"]
            factory = lambda p: make_graph_lf(df_a, p["threshold"], p.get("min_component_size",3))
        else:
            raise ValueError("Unsupported LF in dev-tuning.")
        best, f1 = tune_lf_on_dev(lambda p: factory(p), grid, df_a, df_b, feature_cols)
        results[spec["name"]] = {"best": best, "dev_f1": f1}

    wr = MDWriter(cfg["output"]["md"])
    wr.title("Dev-Set Tuning Results")
    wr.section("Best Parameters")
    wr.bullets({k: str(v) for k,v in results.items()})
    wr.save()

def run_tune_kfold(cfg):
    """Run K-Fold CV tuning for selected LFs."""
    df_tr, df_te, feature_cols = load_pair_data(cfg["data"]["train"], cfg["data"]["test"], cfg["data"].get("exclude"))
    impute_and_cast(df_tr, feature_cols); impute_and_cast(df_te, feature_cols)
    results = {}
    for spec in cfg["tuning"]["lfs"]:
        t = spec["type"].lower()
        if t == "average":
            builder = lambda p, dref: make_average_lf(feature_cols, p["high"], p["low"])
        elif t == "median":
            builder = lambda p, dref: make_median_lf(feature_cols, p["high"], p["low"])
        elif t == "graph":
            builder = lambda p, dref: make_graph_lf(dref, p["threshold"], p.get("min_component_size",3))
        else:
            raise ValueError("Unsupported LF in kfold-tuning.")
        best, mean_f1 = cv_tune_lf(df_tr, feature_cols, spec["grid"], builder, n_splits=cfg["tuning"].get("folds",5))
        results[spec["name"]] = {"best": best, "cv_f1": mean_f1}

    wr = MDWriter(cfg["output"]["md"])
    wr.title("K-Fold CV Tuning Results")
    wr.section("Best Parameters")
    wr.bullets({k: str(v) for k,v in results.items()})
    wr.save()

def dispatch(cfg):
    """Dispatch a config dict to the appropriate runner."""
    task = cfg["task"].lower()
    if task == "supervised":
        run_supervised(cfg)
    elif task == "weak":
        run_weak(cfg)
    elif task == "tune_dev":
        run_tune_dev(cfg)
    elif task == "tune_kfold":
        run_tune_kfold(cfg)
    else:
        raise ValueError(f"Unknown task: {task}")

def main():
    """Entry point for YAML-driven experiments."""
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    args = p.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    dispatch(cfg)

if __name__ == "__main__":
    main()
