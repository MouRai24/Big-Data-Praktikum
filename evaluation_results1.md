## Verwendete Parameter & Schwellenwerte
- Average LF thresholds: DELTA_H=0.9, DELTA_L=0.1
- Variance LF thresholds: DELTA_H=0.9, DELTA_L=0.1, feature j_star=language_containment
- Weighted LF thresholds: HIGH=0.8, LOW=0.2
- RandomForest class_weight='balanced'

Coverage: 6.4%
--- lf_average ---
              precision    recall  f1-score   support

   Non-Match      0.965     1.000     0.982    123721
       Match      0.943     0.093     0.169      4943

    accuracy                          0.965    128664
   macro avg      0.954     0.546     0.576    128664
weighted avg      0.964     0.965     0.951    128664


Coverage: 87.9%
--- lf_variance ---
              precision    recall  f1-score   support

   Non-Match      0.969     0.537     0.691    123721
       Match      0.046     0.565     0.086      4943

    accuracy                          0.538    128664
   macro avg      0.508     0.551     0.388    128664
weighted avg      0.933     0.538     0.668    128664


Coverage: 39.7%
--- lf_weighted ---
              precision    recall  f1-score   support

   Non-Match      0.964     0.784     0.864    123721
       Match      0.045     0.258     0.077      4943

    accuracy                          0.763    128664
   macro avg      0.505     0.521     0.471    128664
weighted avg      0.928     0.763     0.834    128664


Coverage (Snorkel Combined): 93.5%
=== Snorkel_Combined ===
              precision    recall  f1-score   support

   Non-Match      0.969     0.525     0.681    123721
       Match      0.052     0.554     0.094      4943

   micro avg      0.564     0.526     0.544    128664
   macro avg      0.510     0.540     0.388    128664
weighted avg      0.934     0.526     0.659    128664

