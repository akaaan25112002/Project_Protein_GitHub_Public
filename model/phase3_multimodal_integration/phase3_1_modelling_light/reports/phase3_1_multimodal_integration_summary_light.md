
# Phase 3.1 — Multimodal Integration Modelling Summary

## Objective

Phase 3.1 compared three feature settings on the same shared multimodal split:

1. Protein-only ProtBERT sliding-window embeddings
2. Genomic-only K3 + K4 + Basic regulatory features
3. Combined Protein + Genomic features

The goal was to test whether multimodal integration improves T2D-associated gene/protein classification beyond either single modality alone.

## Computational Note

A lightweight GridSearchCV was used for this phase to ensure Colab stability.
The same search protocol was applied consistently across feature settings, making the modality comparison fair.
LightGBM was selectively skipped for high-dimensional settings when needed due to runtime constraints.

## Dataset

Shared multimodal genes: 1806

Train: 1264
Validation: 271
Test: 271

Protein features: 1024
Genomic features: 356
Combined features: 1380

## Official Model Selection

The official model was selected using validation ROC-AUC.

Selected feature set:
Combined Protein+Genomic

Selected modality:
multimodal

Selected model:
SVM RBF

## Official Test Performance

- Accuracy: 0.6642
- Precision: 0.6774
- Recall/Sensitivity: 0.6222
- Specificity: 0.7059
- F1: 0.6486
- ROC-AUC: 0.7290
- PR-AUC: 0.7573
- MCC: 0.3293

Confusion matrix:
- TN: 96
- FP: 40
- FN: 51
- TP: 84

## Best Model per Modality

             feature_set   modality       model dataset  accuracy  precision  recall_sensitivity  specificity       f1  roc_auc   pr_auc      mcc  tn  fp  fn  tp
Combined Protein+Genomic multimodal     SVM RBF    test  0.664207   0.677419            0.622222     0.705882 0.648649 0.728976 0.757253 0.329290  96  40  51  84
Protein-only ProtBERT-SW    protein     SVM RBF    test  0.664207   0.654930            0.688889     0.639706 0.671480 0.727397 0.743341 0.328971  87  49  42  93
  Genomic-only K3K4Basic    genomic Soft Voting    test  0.642066   0.682692            0.525926     0.757353 0.594142 0.655392 0.653991 0.291256 103  33  64  71

## Interpretation

If the combined Protein + Genomic feature set outperforms both protein-only and genomic-only settings on the held-out test set, this supports multimodal integration.

If the combined model does not outperform the best single modality, this suggests either:
- the modalities are not adding independent signal under raw feature concatenation,
- the combined feature dimensionality is too high for the dataset size,
- stronger regularization or dimensionality reduction may be needed,
- or late fusion / stacking may be more appropriate than raw feature concatenation.

## Next Step

The next step is to interpret the Phase 3.1 results and decide whether to:
1. keep raw feature concatenation,
2. try PCA-reduced integration,
3. try score-level late fusion,
4. or add DNABERT-style genomic embeddings.
