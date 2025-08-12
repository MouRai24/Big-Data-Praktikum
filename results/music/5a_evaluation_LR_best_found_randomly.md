# Weak Supervision Evaluation
## LFs
- lf_1: lf_average[h=0.8,l=0.2]
- lf_2: lf_median[h=0.75,l=0.25]
- lf_3: lf_graph[t>=0.8,min=3]

## lf_average[h=0.8,l=0.2]
Coverage: 61.329%
```
precision    recall  f1-score   support

   Non-Match      0.978     0.999     0.988    123721
       Match      0.948     0.436     0.597      4943

    accuracy                          0.977    128664
   macro avg      0.963     0.718     0.793    128664
weighted avg      0.977     0.977     0.973    128664
```

## lf_median[h=0.75,l=0.25]
Coverage: 98.030%
```
precision    recall  f1-score   support

   Non-Match      0.978     0.998     0.988    123721
       Match      0.903     0.451     0.601      4943

    accuracy                          0.977    128664
   macro avg      0.941     0.724     0.795    128664
weighted avg      0.976     0.977     0.973    128664
```

## lf_graph[t>=0.8,min=3]
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.994     0.999     0.996    123721
       Match      0.966     0.841     0.899      4943

    accuracy                          0.993    128664
   macro avg      0.980     0.920     0.948    128664
weighted avg      0.993     0.993     0.993    128664
```

## Snorkel Combined
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.993     0.998     0.995    123721
       Match      0.933     0.831     0.879      4943

    accuracy                          0.991    128664
   macro avg      0.963     0.914     0.937    128664
weighted avg      0.991     0.991     0.991    128664
```

