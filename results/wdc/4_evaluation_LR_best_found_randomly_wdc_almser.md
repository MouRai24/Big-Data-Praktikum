# Weak Supervision Evaluation
## LFs
- lf_1: lf_average[h=0.8,l=0.2]
- lf_2: lf_median[h=0.75,l=0.25]
- lf_3: lf_graph[t>=0.75,min=3]

## lf_average[h=0.8,l=0.2]
Coverage: 57.824%
```
precision    recall  f1-score   support

   Non-Match      0.973     0.689     0.807     21993
       Match      0.120     0.693     0.205      1348

    accuracy                          0.689     23341
   macro avg      0.547     0.691     0.506     23341
weighted avg      0.924     0.689     0.772     23341
```

## lf_median[h=0.75,l=0.25]
Coverage: 82.782%
```
precision    recall  f1-score   support

   Non-Match      0.977     0.673     0.797     21993
       Match      0.122     0.741     0.210      1348

    accuracy                          0.677     23341
   macro avg      0.550     0.707     0.504     23341
weighted avg      0.928     0.677     0.763     23341
```

## lf_graph[t>=0.75,min=3]
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.981     0.821     0.894     21993
       Match      0.204     0.747     0.320      1348

    accuracy                          0.817     23341
   macro avg      0.593     0.784     0.607     23341
weighted avg      0.937     0.817     0.861     23341
```

## Snorkel Combined
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.983     0.763     0.859     21993
       Match      0.168     0.780     0.276      1348

    accuracy                          0.764     23341
   macro avg      0.575     0.771     0.567     23341
weighted avg      0.936     0.764     0.825     23341
```

