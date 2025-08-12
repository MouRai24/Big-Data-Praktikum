# Weak Supervision Evaluation
## LFs
- lf_1: lf_average[h=0.9,l=0.1]
- lf_2: lf_variance[j=language_containment,h=0.9,l=0.1]
- lf_3: lf_weighted[h=0.8,l=0.2]
- lf_4: lf_graph[t>=0.5,min=3]

## lf_average[h=0.9,l=0.1]
Coverage: 6.423%
```
precision    recall  f1-score   support

   Non-Match      0.965     1.000     0.982    123721
       Match      0.943     0.093     0.169      4943

    accuracy                          0.965    128664
   macro avg      0.954     0.546     0.576    128664
weighted avg      0.964     0.965     0.951    128664
```

## lf_variance[j=language_containment,h=0.9,l=0.1]
Coverage: 87.888%
```
precision    recall  f1-score   support

   Non-Match      0.969     0.537     0.691    123721
       Match      0.046     0.565     0.086      4943

    accuracy                          0.538    128664
   macro avg      0.508     0.551     0.388    128664
weighted avg      0.933     0.538     0.668    128664
```

## lf_weighted[h=0.8,l=0.2]
Coverage: 39.698%
```
precision    recall  f1-score   support

   Non-Match      0.964     0.784     0.864    123721
       Match      0.045     0.258     0.077      4943

    accuracy                          0.763    128664
   macro avg      0.505     0.521     0.471    128664
weighted avg      0.928     0.763     0.834    128664
```

## lf_graph[t>=0.5,min=3]
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.998     0.681     0.810    123721
       Match      0.109     0.972     0.195      4943

    accuracy                          0.692    128664
   macro avg      0.553     0.827     0.502    128664
weighted avg      0.964     0.692     0.786    128664
```

## Snorkel Combined
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.972     0.578     0.725    123721
       Match      0.052     0.578     0.095      4943

    accuracy                          0.578    128664
   macro avg      0.512     0.578     0.410    128664
weighted avg      0.936     0.578     0.701    128664
```

