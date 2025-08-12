import numpy as np

def impute_and_cast(df, feature_cols):
    """Replace sentinel values with NaN, cast to float, and fill missing values with 0."""
    df[feature_cols] = df[feature_cols].replace(-1, np.nan).astype(float).fillna(0.0)
    return df
