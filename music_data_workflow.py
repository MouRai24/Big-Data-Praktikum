#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Weak Supervision Workflow auf dem Musik-Datensatz
================================================
1) Laden & Vorverarbeiten (train/test)
2) Definition der 3 Labeling-Functions
3) Pseudolabels erzeugen & Endmodell trainieren EINZELN pro LF
4) Pseudolabels erzeugen & Endmodell trainieren KOMBINIEREND (Snorkel LabelModel)
5) Evaluation aller Modelle auf dem Test-Set
"""

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

import pandas as pd
import numpy as np

from snorkel.labeling import labeling_function, PandasLFApplier
from snorkel.labeling.model import LabelModel  
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics  import classification_report




def main():
    out_fp = open("evaluation_results.md", "w")

    # 1) Laden & Preprocessing
    # --------------------------------------------------
    print("1) Daten laden …")
    df_train = pd.read_csv('linkage_problems/Music/train_pairs_fv.csv')
    df_test  = pd.read_csv('linkage_problems/Music/test_pairs_fv.csv')
    print(f"   → Train: {df_train.shape[0]}×{df_train.shape[1]}")
    print(f"   → Test : {df_test.shape[0]}×{df_test.shape[1]}\n")

    # Filter nur echte Labels 0/1 im Test
    df_test = df_test[df_test["label"].isin([0,1])].copy()
    y_test  = df_test["label"].values

    # Feature-Spalten extrahieren
    exclude = ["source_id","target_id","pair_id","source","target",
               "label","unsupervised_label","agg_score"]
    feature_cols = [c for c in df_train.columns if c not in exclude]
    print(f"   → {len(feature_cols)} Similarity-Features\n")

    # -1 → NaN, Cast float, NaN→0
    for df in (df_train, df_test):
        df[feature_cols] = (
            df[feature_cols]
            .replace(-1, np.nan)
            .astype(float)
            .fillna(0)
        )
    print("   → Missing-Werte imputiert (–1→0), alle Features float\n")

    X_train = df_train[feature_cols].values
    X_test  = df_test[feature_cols].values

    # --------------------------------------------------
    # 2) Labeling-Functions definieren
    # --------------------------------------------------
    print("2) Labeling-Functions definieren …")
    DELTA_H, DELTA_L = 0.9, 0.1
    WEIGHTED_HIGH, WEIGHTED_LOW = 0.8, 0.2

    @labeling_function(name="lf_average")
    def lf_average(x):
        m = x[feature_cols].mean()
        if m >= DELTA_H: return 1
        if m <= DELTA_L: return 0
        return -1

    variances = df_train[feature_cols].var()
    j_star    = variances.idxmax()
    @labeling_function(name="lf_variance")
    def lf_variance(x):
        v = x[j_star]
        if v >= DELTA_H: return 1
        if v <= DELTA_L: return 0
        return -1

    uniqueness = variances / variances.sum()
    @labeling_function(name="lf_weighted")
    def lf_weighted(x):
        score = np.dot(uniqueness.values, x[feature_cols].values)
        if score >= WEIGHTED_HIGH: return 1
        if score <= WEIGHTED_LOW: return 0
        return -1

    lfs = [lf_average, lf_variance, lf_weighted]
    print("   → LFs:", ", ".join(lf.name for lf in lfs), "\n")

    # --------------------------------------------------
    # 3) Endmodell-Workflow EINZELN pro LF
    # --------------------------------------------------
    print("3) Endmodell-Training pro einzelne LF:\n")
    out_fp.write("## Verwendete Parameter & Schwellenwerte\n")
    out_fp.write(f"- Average LF thresholds: DELTA_H={DELTA_H}, DELTA_L={DELTA_L}\n")
    out_fp.write(f"- Variance LF thresholds: DELTA_H={DELTA_H}, DELTA_L={DELTA_L}, feature j_star={j_star}\n")
    out_fp.write(f"- Weighted LF thresholds: HIGH={WEIGHTED_HIGH}, LOW={WEIGHTED_LOW}\n")
    for lf in lfs:
        print(f"--- {lf.name} ---")
        # 3.1 Pseudolabels auf Train
        applier = PandasLFApplier([lf])
        L_train = applier.apply(df_train).ravel()  # Form (n_train,)
        mask_tr = L_train != -1
        print(f"   Train-Coverage: {mask_tr.mean()*100:.1f}%")
        cov = mask_tr.mean()*100
        print(f"   Train-Coverage: {cov:.1f}%")
        out_fp.write(f"Coverage: {cov:.1f}%\n")

        # 3.2 RF auf den Pseudolabels trainieren
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X_train[mask_tr], L_train[mask_tr])

        # 3.3 Evaluation auf Test
        y_pred = clf.predict(X_test)
        # Report
        print(classification_report(
            y_test, y_pred,
            labels=[0,1],
            target_names=["Non-Match","Match"],
            digits=3,
            zero_division=0
        ))
        print()
        # 3.3 Evaluation auf Test
        y_pred = clf.predict(X_test)
        report = classification_report(
            y_test, y_pred,
            labels=[0,1],
            target_names=["Non-Match","Match"],
            digits=3,
            zero_division=0
        )
        print(report)
        out_fp.write(f"--- {lf.name} ---\n{report}\n\n")

    # --------------------------------------------------
    # 4) Endmodell-Workflow KOMBINIEREND (Snorkel LabelModel)
    # --------------------------------------------------
    print("4) Endmodell-Training mit Snorkel LabelModel:\n")
    # 4.1 Label-Matrix und LabelModel
    applier_all = PandasLFApplier(lfs)
    L_train_all = applier_all.apply(df_train)
    label_model = LabelModel(cardinality=2, verbose=False)
    label_model.fit(L_train=L_train_all, n_epochs=200, lr=0.01)
    # 4.2 Pseudolabels & RF-Training
    y_train_pseudo = label_model.predict(L=L_train_all)
    print(f"   Pseudolabels Coverage: { (y_train_pseudo!=-1).mean()*100:.1f}%")
    cov_all = (y_train_pseudo != -1).mean()*100
    print(f"   Pseudolabels Coverage: {cov_all:.1f}%")
    out_fp.write(f"Coverage (Snorkel Combined): {cov_all:.1f}%\n")
    clf_all = RandomForestClassifier(n_estimators=100, random_state=42)
    clf_all.fit(X_train, y_train_pseudo)

    # 4.3 Evaluation auf Test
    y_pred_all = clf_all.predict(X_test)
    print(classification_report(
        y_test, y_pred_all,
        labels=[0,1],
        target_names=["Non-Match","Match"],
        digits=3,
        zero_division=0
    ))
    combined_report = classification_report(
        y_test, y_pred_all,
        labels=[0,1],
        target_names=["Non-Match","Match"],
        digits=3,
        zero_division=0
    )
    print(combined_report)
    out_fp.write("=== Snorkel_Combined ===\n" + combined_report + "\n")

# At the very end of main(), before it returns, close the file:
    out_fp.close()


if __name__ == "__main__":
    main()

