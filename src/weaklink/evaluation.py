from sklearn.metrics import classification_report

def eval_report(y_true, y_pred, target_names=("Non-Match","Match"), digits=3):
    """Return a classification_report string for binary linkage labels."""
    return classification_report(y_true, y_pred, labels=[0,1], target_names=list(target_names), digits=digits, zero_division=0)
