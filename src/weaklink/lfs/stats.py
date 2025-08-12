import numpy as np
from snorkel.labeling import labeling_function

def make_average_lf(feature_cols, high: float, low: float):
    """Return a labeling function that votes by the mean of similarity features."""
    @labeling_function(name=f"lf_average[h={high},l={low}]")
    def lf(x):
        m = x[feature_cols].mean()
        if m >= high: return 1
        if m <= low: return 0
        return -1
    return lf

def make_median_lf(feature_cols, high: float, low: float):
    """Return a labeling function that votes by the median of similarity features."""
    @labeling_function(name=f"lf_median[h={high},l={low}]")
    def lf(x):
        m = float(np.median(x[feature_cols]))
        if m >= high: return 1
        if m <= low: return 0
        return -1
    return lf

def make_variance_pick_lf(feature_cols, var_series, high: float, low: float):
    """Return a labeling function that votes by the feature with highest variance."""
    j_star = var_series.idxmax()
    @labeling_function(name=f"lf_variance[j={j_star},h={high},l={low}]")
    def lf(x):
        v = x[j_star]
        if v >= high: return 1
        if v <= low: return 0
        return -1
    return lf

def make_weighted_mean_lf(feature_cols, weights, high: float, low: float):
    """Return a labeling function that votes by a weighted mean of features."""
    w = weights.values if hasattr(weights, "values") else np.asarray(weights)
    @labeling_function(name=f"lf_weighted[h={high},l={low}]")
    def lf(x):
        s = float(np.dot(w, x[feature_cols].values))
        if s >= high: return 1
        if s <= low: return 0
        return -1
    return lf

def make_count_high_lf(feature_cols, threshold_value: float, min_count: int, max_count_nonmatch: int):
    """Return a labeling function that votes by counting features above a threshold."""
    @labeling_function(name=f"lf_count[val>={threshold_value},min={min_count}]")
    def lf(x):
        cnt = int((x[feature_cols] >= threshold_value).sum())
        if cnt >= min_count: return 1
        if cnt <= max_count_nonmatch: return 0
        return -1
    return lf

def make_low_all_lf(feature_cols, max_value: float):
    """Return a labeling function that votes 0 if all features are below a max value."""
    @labeling_function(name=f"lf_low_all[max<={max_value}]")
    def lf(x):
        return 0 if float(x[feature_cols].max()) <= max_value else -1
    return lf

def make_single_feature_lf(feature_name: str, high: float, low: float):
    """Return a labeling function that votes using a single feature column; abstains if the column is missing or NaN."""
    from snorkel.labeling import labeling_function
    import math

    @labeling_function(name=f"lf_{feature_name}[h={high},l={low}]")
    def lf(x):
        v = x.get(feature_name, None)
        if v is None or (isinstance(v, float) and math.isnan(v)):
            return -1
        if v >= high: return 1
        if v <= low: return 0
        return -1
    return lf

