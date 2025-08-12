import numpy as np
from snorkel.labeling import PandasLFApplier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

def tune_lf_on_dev(lf_factory, param_grid, df_train_ref, df_dev_ref, feature_cols, sample_train=20000, sample_dev=5000, random_state=42):
    """Grid-search thresholds for one LF using a small dev split and return (best_params, best_f1)."""
    tr_sub = df_train_ref.sample(n=min(sample_train, len(df_train_ref)), random_state=random_state).reset_index(drop=True)
    dev_sub = df_dev_ref.sample(n=min(sample_dev, len(df_dev_ref)), random_state=random_state).reset_index(drop=True)
    y_dev = dev_sub["label"].values
    best, best_f1 = None, -1.0
    for params in param_grid:
        lf = lf_factory(params)
        L_tr = PandasLFApplier([lf]).apply(tr_sub).ravel()
        mask_tr = L_tr != -1
        if mask_tr.sum() < 10 or len(np.unique(L_tr[mask_tr])) < 2:
            continue
        clf = LogisticRegression(max_iter=500, class_weight="balanced", random_state=random_state)
        clf.fit(tr_sub.loc[mask_tr, feature_cols], L_tr[mask_tr])
        L_dev = PandasLFApplier([lf]).apply(dev_sub).ravel()
        mask_dev = L_dev != -1
        if mask_dev.sum() == 0:
            continue
        y_pred = clf.predict(dev_sub.loc[mask_dev, feature_cols])
        f1 = f1_score(y_dev[mask_dev], y_pred)
        if f1 > best_f1:
            best, best_f1 = params, float(f1)
    return best, best_f1
