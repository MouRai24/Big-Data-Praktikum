# Weak Supervision Evaluation
## LFs
- lf_1: lf_average[h=0.8,l=0.2]
- lf_2: lf_variance[j=language_containment,h=0.8,l=0.2]
- lf_3: lf_weighted[h=0.75,l=0.25]
- lf_4: lf_graph[t>=0.8,min=3]

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

## lf_variance[j=language_containment,h=0.8,l=0.2]
Coverage: 90.637%
```
precision    recall  f1-score   support

   Non-Match      0.968     0.532     0.686    123721
       Match      0.046     0.565     0.085      4943

    accuracy                          0.533    128664
   macro avg      0.507     0.548     0.386    128664
weighted avg      0.933     0.533     0.663    128664
```

## lf_weighted[h=0.75,l=0.25]
Coverage: 55.819%
```
precision    recall  f1-score   support

   Non-Match      0.964     0.796     0.872    123721
       Match      0.047     0.251     0.079      4943

    accuracy                          0.775    128664
   macro avg      0.505     0.524     0.476    128664
weighted avg      0.929     0.775     0.842    128664
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

   Non-Match      0.981     0.607     0.750    123721
       Match      0.066     0.700     0.121      4943

    accuracy                          0.611    128664
   macro avg      0.524     0.653     0.436    128664
weighted avg      0.945     0.611     0.726    128664
```

