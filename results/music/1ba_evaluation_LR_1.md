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

   Non-Match      0.974     0.998     0.986    123721
       Match      0.879     0.325     0.475      4943

    accuracy                          0.972    128664
   macro avg      0.926     0.662     0.730    128664
weighted avg      0.970     0.972     0.966    128664
```

## lf_variance[j=language_containment,h=0.9,l=0.1]
Coverage: 87.888%
```
precision    recall  f1-score   support

   Non-Match      0.968     0.531     0.686    123721
       Match      0.046     0.565     0.085      4943

    accuracy                          0.533    128664
   macro avg      0.507     0.548     0.386    128664
weighted avg      0.933     0.533     0.663    128664
```

## lf_weighted[h=0.8,l=0.2]
Coverage: 39.698%
```
precision    recall  f1-score   support

   Non-Match      0.964     0.797     0.873    123721
       Match      0.049     0.265     0.083      4943

    accuracy                          0.776    128664
   macro avg      0.507     0.531     0.478    128664
weighted avg      0.929     0.776     0.842    128664
```

## lf_graph[t>=0.5,min=3]
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.998     0.632     0.774    123721
       Match      0.096     0.975     0.174      4943

    accuracy                          0.645    128664
   macro avg      0.547     0.804     0.474    128664
weighted avg      0.964     0.645     0.751    128664
```

## Snorkel Combined
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.970     0.561     0.711    123721
       Match      0.050     0.573     0.091      4943

    accuracy                          0.561    128664
   macro avg      0.510     0.567     0.401    128664
weighted avg      0.935     0.561     0.687    128664
```

