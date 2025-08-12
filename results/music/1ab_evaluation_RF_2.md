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

   Non-Match      0.973     1.000     0.986    123721
       Match      0.988     0.300     0.461      4943

    accuracy                          0.973    128664
   macro avg      0.980     0.650     0.723    128664
weighted avg      0.973     0.973     0.966    128664
```

## lf_variance[j=language_containment,h=0.8,l=0.2]
Coverage: 90.637%
```
precision    recall  f1-score   support

   Non-Match      0.968     0.531     0.686    123721
       Match      0.046     0.565     0.085      4943

    accuracy                          0.532    128664
   macro avg      0.507     0.548     0.385    128664
weighted avg      0.933     0.532     0.663    128664
```

## lf_weighted[h=0.75,l=0.25]
Coverage: 55.819%
```
precision    recall  f1-score   support

   Non-Match      0.964     0.791     0.869    123721
       Match      0.046     0.255     0.079      4943

    accuracy                          0.770    128664
   macro avg      0.505     0.523     0.474    128664
weighted avg      0.928     0.770     0.839    128664
```

## lf_graph[t>=0.8,min=3]
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.973     1.000     0.986    123721
       Match      0.997     0.314     0.478      4943

    accuracy                          0.974    128664
   macro avg      0.985     0.657     0.732    128664
weighted avg      0.974     0.974     0.967    128664
```

## Snorkel Combined
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.980     0.622     0.761    123721
       Match      0.067     0.681     0.122      4943

    accuracy                          0.624    128664
   macro avg      0.523     0.651     0.442    128664
weighted avg      0.945     0.624     0.736    128664
```

