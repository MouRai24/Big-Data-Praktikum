import pandas as pd

EXCLUDE_DEFAULT = ["Unnamed: 0","source_id","target_id","pair_id","source","target","label","unsupervised_label","agg_score"]

def load_pair_data(train_csv: str, test_csv: str, add_exclude=None):
    """Load train/test CSVs for pairwise linkage and return (df_train, df_test, feature_cols)."""
    df_tr = pd.read_csv(train_csv)
    df_te = pd.read_csv(test_csv)
    df_te = df_te[df_te["label"].isin([0,1])].copy()
    exclude = EXCLUDE_DEFAULT + (list(add_exclude) if add_exclude else [])
    feature_cols = [c for c in df_tr.columns if c not in set(exclude)]
    return df_tr, df_te, feature_cols
