from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def make_model(kind: str, **kwargs):
    """Return a scikit-learn classifier by name."""
    if kind.lower() in {"lr","logreg","logistic"}:
        return LogisticRegression(max_iter=kwargs.get("max_iter",1000),
                                  class_weight=kwargs.get("class_weight","balanced"),
                                  random_state=kwargs.get("random_state",42))
    if kind.lower() in {"rf","randomforest"}:
        return RandomForestClassifier(n_estimators=kwargs.get("n_estimators",100),
                                      random_state=kwargs.get("random_state",42),
                                      class_weight=kwargs.get("class_weight",None))
    raise ValueError(f"Unknown model: {kind}")
