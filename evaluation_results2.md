## Verwendete Parameter & Schwellenwerte
- Average LF thresholds: DELTA_H=0.8, DELTA_L=0.2
- Variance LF thresholds: DELTA_H=0.8, DELTA_L=0.2, feature j_star=language_containment
- Weighted LF thresholds: HIGH=0.75, LOW=0.25

Coverage: 61.3%
--- lf_average ---
              precision    recall  f1-score   support

   Non-Match      0.973     1.000     0.986    123721
       Match      0.988     0.300     0.461      4943

    accuracy                          0.973    128664
   macro avg      0.980     0.650     0.723    128664
weighted avg      0.973     0.973     0.966    128664


Coverage: 90.6%
--- lf_variance ---
              precision    recall  f1-score   support

   Non-Match      0.968     0.531     0.686    123721
       Match      0.046     0.565     0.085      4943

    accuracy                          0.532    128664
   macro avg      0.507     0.548     0.385    128664
weighted avg      0.933     0.532     0.663    128664


Coverage: 55.8%
--- lf_weighted ---
              precision    recall  f1-score   support

   Non-Match      0.964     0.791     0.869    123721
       Match      0.046     0.255     0.079      4943

    accuracy                          0.770    128664
   macro avg      0.505     0.523     0.474    128664
weighted avg      0.928     0.770     0.839    128664


Coverage (Snorkel Combined): 98.7%
=== Snorkel_Combined ===
              precision    recall  f1-score   support

   Non-Match      0.973     0.612     0.751    123721
       Match      0.055     0.554     0.101      4943

   micro avg      0.616     0.610     0.613    128664
   macro avg      0.514     0.583     0.426    128664
weighted avg      0.938     0.610     0.726    128664

