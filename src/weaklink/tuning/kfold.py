import numpy as np
from snorkel.labeling import PandasLFApplier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score

def cv_tune_lf(df_train_ref, feature_cols, param_grid, lf_builder, n_splits=5, random_state=42):
    """K-Fold CV tuning for one LF; lf_builder(params, df_split) must return an LF built on the split."""
    X = df_train_ref[feature_cols]
    y = df_train_ref["label"].values
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    best_param, best_mean = None, -1.0
    for params in param_grid:
        scores = []
        for tr_idx, va_idx in skf.split(X, y):
            df_tr = df_train_ref.iloc[tr_idx]
            df_va = df_train_ref.iloc[va_idx]
            lf = lf_builder(params, df_tr)
            L_tr = PandasLFApplier([lf]).apply(df_tr).ravel()
            mask_tr = L_tr != -1
            if len(np.unique(L_tr[mask_tr])) < 2:
                continue
            clf = LogisticRegression(max_iter=500, class_weight="balanced", random_state=random_state)
            clf.fit(df_tr.loc[mask_tr, feature_cols], L_tr[mask_tr])
            L_va = PandasLFApplier([lf]).apply(df_va).ravel()
            mask_va = L_va != -1
            if mask_va.sum() == 0:
                continue
            y_pred = clf.predict(df_va.loc[mask_va, feature_cols])
            scores.append(f1_score(df_va["label"].values[mask_va], y_pred))
        if scores:
            m = float(np.mean(scores))
            if m > best_mean:
                best_param, best_mean = params, m
    return best_param, best_mean
