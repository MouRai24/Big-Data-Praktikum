import numpy as np
from snorkel.labeling import PandasLFApplier
from snorkel.labeling.model import LabelModel

def apply_lfs(df, lfs):
    """Apply a list of labeling functions and return label matrix."""
    applier = PandasLFApplier(lfs)
    return applier.apply(df)

def combine_with_label_model(L, cardinality=2, n_epochs=200, lr=0.01):
    """Fit Snorkel LabelModel and return pseudo-labels with -1 for abstains."""
    lm = LabelModel(cardinality=cardinality, verbose=False)
    lm.fit(L_train=L, n_epochs=n_epochs, lr=lr)
    return lm.predict(L=L)

def mask_labeled(y_pseudo):
    """Return boolean mask for non-abstained labels."""
    return y_pseudo != -1

def coverage(y_pseudo):
    """Return coverage ratio of non-abstained labels."""
    m = mask_labeled(y_pseudo)
    return float(np.mean(m)) if len(m) else 0.0
