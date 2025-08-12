# Weak Supervision Evaluation
## LFs
- lf_1: lf_title_jaccard[h=0.85,l=0.15]
- lf_2: lf_artist_jaccard[h=0.8,l=0.2]
- lf_3: lf_count[val>=0.8,min=10]
- lf_4: lf_median[h=0.75,l=0.25]
- lf_5: lf_low_all[max<=0.2]
- lf_6: lf_graph[t>=0.5,min=2]

## lf_title_jaccard[h=0.85,l=0.15]
Coverage: 86.597%
```
precision    recall  f1-score   support

   Non-Match      0.972     1.000     0.986    123721
       Match      0.971     0.288     0.445      4943

    accuracy                          0.972    128664
   macro avg      0.972     0.644     0.715    128664
weighted avg      0.972     0.972     0.965    128664
```

## lf_artist_jaccard[h=0.8,l=0.2]
Coverage: 97.327%
```
precision    recall  f1-score   support

   Non-Match      0.978     0.986     0.982    123721
       Match      0.563     0.456     0.504      4943

    accuracy                          0.966    128664
   macro avg      0.771     0.721     0.743    128664
weighted avg      0.962     0.966     0.964    128664
```

## lf_count[val>=0.8,min=10]
Coverage: 42.616%
```
precision    recall  f1-score   support

   Non-Match      0.997     0.764     0.865    123721
       Match      0.138     0.948     0.241      4943

    accuracy                          0.771    128664
   macro avg      0.568     0.856     0.553    128664
weighted avg      0.964     0.771     0.841    128664
```

## lf_median[h=0.75,l=0.25]
Coverage: 98.030%
```
precision    recall  f1-score   support

   Non-Match      0.975     0.999     0.987    123721
       Match      0.925     0.370     0.529      4943

    accuracy                          0.975    128664
   macro avg      0.950     0.685     0.758    128664
weighted avg      0.973     0.975     0.969    128664
```

## lf_low_all[max<=0.2]
Coverage: 0.111%
```
precision    recall  f1-score   support

   Non-Match      0.962     1.000     0.980    123721
       Match      0.000     0.000     0.000      4943

    accuracy                          0.962    128664
   macro avg      0.481     0.500     0.490    128664
weighted avg      0.925     0.962     0.943    128664
```

## lf_graph[t>=0.5,min=2]
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.999     0.681     0.810    123721
       Match      0.109     0.975     0.196      4943

    accuracy                          0.692    128664
   macro avg      0.554     0.828     0.503    128664
weighted avg      0.964     0.692     0.786    128664
```

## Snorkel Combined
Coverage: 100.000%
```
precision    recall  f1-score   support

   Non-Match      0.999     0.700     0.823    123721
       Match      0.115     0.976     0.206      4943

    accuracy                          0.711    128664
   macro avg      0.557     0.838     0.515    128664
weighted avg      0.965     0.711     0.799    128664
```

