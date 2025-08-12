# Weak Supervision Evaluation
## LFs
- lf_1: lf_average[h=0.8,l=0.2]
- lf_2: lf_variance[j=brand_overlap,h=0.8,l=0.2]
- lf_3: lf_weighted[h=0.75,l=0.25]
- lf_4: lf_graph[t>=0.8,min=3]

## lf_average[h=0.8,l=0.2]
Coverage: 57.824%
```
precision    recall  f1-score   support

   Non-Match      0.976     0.648     0.779     21993
       Match      0.114     0.741     0.198      1348

    accuracy                          0.653     23341
   macro avg      0.545     0.694     0.488     23341
weighted avg      0.926     0.653     0.745     23341
```

## lf_variance[j=brand_overlap,h=0.8,l=0.2]
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.978     0.552     0.706     21993
       Match      0.098     0.797     0.175      1348

    accuracy                          0.567     23341
   macro avg      0.538     0.675     0.441     23341
weighted avg      0.927     0.567     0.675     23341
```

## lf_weighted[h=0.75,l=0.25]
Coverage: 76.043%
```
precision    recall  f1-score   support

   Non-Match      0.976     0.599     0.742     21993
       Match      0.104     0.757     0.182      1348

    accuracy                          0.608     23341
   macro avg      0.540     0.678     0.462     23341
weighted avg      0.925     0.608     0.710     23341
```

## lf_graph[t>=0.8,min=3]
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.961     0.955     0.958     21993
       Match      0.337     0.370     0.353      1348

    accuracy                          0.922     23341
   macro avg      0.649     0.663     0.656     23341
weighted avg      0.925     0.922     0.923     23341
```

## Snorkel Combined
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.978     0.552     0.706     21993
       Match      0.099     0.800     0.176      1348

    accuracy                          0.567     23341
   macro avg      0.538     0.676     0.441     23341
weighted avg      0.927     0.567     0.675     23341
```

