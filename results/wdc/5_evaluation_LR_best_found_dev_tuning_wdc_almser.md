# Weak Supervision Evaluation
## LFs
- lf_1: lf_average[h=0.9,l=0.1]
- lf_2: lf_median[h=0.8,l=0.2]
- lf_3: lf_graph[t>=0.85,min=3]

## lf_average[h=0.9,l=0.1]
Coverage: 43.271%
```
precision    recall  f1-score   support

   Non-Match      0.974     0.711     0.822     21993
       Match      0.128     0.692     0.216      1348

    accuracy                          0.710     23341
   macro avg      0.551     0.701     0.519     23341
weighted avg      0.925     0.710     0.787     23341
```

## lf_median[h=0.8,l=0.2]
Coverage: 79.914%
```
precision    recall  f1-score   support

   Non-Match      0.977     0.672     0.796     21993
       Match      0.122     0.746     0.210      1348

    accuracy                          0.676     23341
   macro avg      0.550     0.709     0.503     23341
weighted avg      0.928     0.676     0.762     23341
```

## lf_graph[t>=0.85,min=3]
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.969     0.955     0.962     21993
       Match      0.403     0.499     0.446      1348

    accuracy                          0.928     23341
   macro avg      0.686     0.727     0.704     23341
weighted avg      0.936     0.928     0.932     23341
```

## Snorkel Combined
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.977     0.589     0.735     21993
       Match      0.103     0.772     0.182      1348

    accuracy                          0.600     23341
   macro avg      0.540     0.681     0.459     23341
weighted avg      0.926     0.600     0.703     23341
```

