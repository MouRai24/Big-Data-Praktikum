# Weak Supervision Evaluation
## LFs
- lf_1: lf_average[h=0.7,l=0.1]
- lf_2: lf_median[h=0.6,l=0.2]
- lf_3: lf_graph[t>=0.75,min=3]

## lf_average[h=0.7,l=0.1]
Coverage: 6.474%
```
precision    recall  f1-score   support

   Non-Match      0.988     0.998     0.993    123721
       Match      0.918     0.689     0.787      4943

    accuracy                          0.986    128664
   macro avg      0.953     0.843     0.890    128664
weighted avg      0.985     0.986     0.985    128664
```

## lf_median[h=0.6,l=0.2]
Coverage: 97.672%
```
precision    recall  f1-score   support

   Non-Match      0.981     0.998     0.989    123721
       Match      0.897     0.504     0.645      4943

    accuracy                          0.979    128664
   macro avg      0.939     0.751     0.817    128664
weighted avg      0.977     0.979     0.976    128664
```

## lf_graph[t>=0.75,min=3]
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.996     0.996     0.996    123721
       Match      0.908     0.911     0.910      4943

    accuracy                          0.993    128664
   macro avg      0.952     0.954     0.953    128664
weighted avg      0.993     0.993     0.993    128664
```

## Snorkel Combined
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.996     0.994     0.995    123721
       Match      0.855     0.901     0.877      4943

    accuracy                          0.990    128664
   macro avg      0.925     0.948     0.936    128664
weighted avg      0.991     0.990     0.990    128664
```

