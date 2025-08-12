# Weak Supervision Evaluation
## LFs
- lf_1: lf_count[val>=0.8,min=10]
- lf_2: lf_median[h=0.75,l=0.25]
- lf_3: lf_low_all[max<=0.2]
- lf_4: lf_graph[t>=0.5,min=2]

## lf_count[val>=0.8,min=10]
Coverage: 93.265%
```
precision    recall  f1-score   support

   Non-Match      0.994     0.533     0.694     21993
       Match      0.111     0.950     0.198      1348

    accuracy                          0.557     23341
   macro avg      0.552     0.741     0.446     23341
weighted avg      0.943     0.557     0.665     23341
```

## lf_median[h=0.75,l=0.25]
Coverage: 82.782%
```
precision    recall  f1-score   support

   Non-Match      0.976     0.675     0.798     21993
       Match      0.121     0.728     0.207      1348

    accuracy                          0.678     23341
   macro avg      0.548     0.702     0.502     23341
weighted avg      0.927     0.678     0.764     23341
```

## lf_low_all[max<=0.2]
Coverage: 0.016%
```
precision    recall  f1-score   support

   Non-Match      0.942     1.000     0.970     21993
       Match      0.000     0.000     0.000      1348

    accuracy                          0.942     23341
   macro avg      0.471     0.500     0.485     23341
weighted avg      0.888     0.942     0.914     23341
```

## lf_graph[t>=0.5,min=2]
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      1.000     0.502     0.668     21993
       Match      0.109     0.997     0.197      1348

    accuracy                          0.531     23341
   macro avg      0.554     0.750     0.433     23341
weighted avg      0.948     0.531     0.641     23341
```

## Snorkel Combined
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.998     0.532     0.694     21993
       Match      0.114     0.981     0.204      1348

    accuracy                          0.558     23341
   macro avg      0.556     0.757     0.449     23341
weighted avg      0.947     0.558     0.666     23341
```

