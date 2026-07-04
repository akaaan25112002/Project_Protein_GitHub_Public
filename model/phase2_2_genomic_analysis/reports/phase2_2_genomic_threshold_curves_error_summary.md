
# Phase 2.2 — Genomic Threshold Tuning, ROC/PR Curves, and Error Analysis

## Objective

Phase 2.2 evaluated the genomic regulatory handcrafted baseline beyond default-threshold testing.
The goals were to tune decision thresholds, compare ROC/PR ranking performance, and analyze errors for the genomic regulatory branch.

## Feature Representation

The selected genomic feature set was:

K3 + K4 + Basic

This feature set includes:
- Basic DNA composition
- GC and AT content
- CpG features
- GC/AT skew
- Positional GC bins
- 3-mer frequencies
- 4-mer frequencies

## Default Threshold Results

The official final genomic model selected in Phase 2.1 was Random Forest based on validation ROC-AUC.

At threshold 0.5, Random Forest achieved:

- Test ROC-AUC: 0.6496
- Test PR-AUC: 0.6327
- Test F1: 0.6406
- Test MCC: 0.2557

Diagnostic testing showed that the best test ROC-AUC model at default threshold was:

- Model: SVM RBF
- Test ROC-AUC: 0.6765
- Test PR-AUC: 0.6504
- Test F1: 0.6620
- Test MCC: 0.2933

This diagnostic result was not used to change the official final model, because model selection was based on validation performance.

## Threshold Tuning

Threshold tuning was performed using the validation set for:
- Random Forest
- SVM RBF
- Logistic Regression

The best tuned test result by MCC was:

- Model: Random Forest
- Tuned for: balanced_accuracy
- Threshold: 0.518
- Test ROC-AUC: 0.6496
- Test PR-AUC: 0.6327
- Test F1: 0.6288
- Test MCC: 0.2769

## Official Genomic Model Error Analysis

The official Random Forest model with validation-tuned MCC threshold achieved:

- Threshold: 0.600
- TP: 39
- TN: 118
- FP: 18
- FN: 96
- F1: 0.4062
- MCC: 0.1920

## Interpretation

The genomic regulatory handcrafted branch produced performance comparable to the protein ProtBERT branch.
This suggests that TSS-proximal regulatory DNA sequences contain meaningful signal for distinguishing T2D-associated genes from strict background genes.

The genomic branch was particularly strong in threshold-based metrics such as F1 and MCC, while the protein branch retained stronger PR-AUC in the best protein setting.
This supports the hypothesis that protein and regulatory DNA representations capture complementary biological signals.

## Next Step

The next recommended step is to compare protein and genomic prediction errors and then prepare for multimodal integration:

Protein embedding + genomic regulatory features

Before integration, the following should be saved:
- Genomic prediction scores
- Protein prediction scores
- Shared gene_id mapping
- Error type tables for both modalities
