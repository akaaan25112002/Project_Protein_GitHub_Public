
# Phase 5 — DNABERT-2 Genomic Foundation Model Extension

## Objective

Phase 5 extended the genomic branch by replacing handcrafted K3/K4/Basic regulatory features with DNABERT-2 embeddings.

The goal was to test whether a genomic foundation model representation improves T2D gene/protein association prediction compared with handcrafted regulatory features.

## Representation

DNABERT-2 model:
zhihan1996/DNABERT-2-117M

Embedding policy:
Base-level sliding window with window size 2048 and stride 1024.
Window embeddings were mean-pooled to obtain one gene-level regulatory sequence embedding.

## Evaluated Settings

1. Genomic-only DNABERT-2
2. Combined ProtBERT-SW + DNABERT-2

## Official DNABERT-2 Genomic-only Model

Selected model:
Random Forest

Test metrics:
- ROC-AUC: 0.6833
- PR-AUC: 0.6838
- F1: 0.5478
- MCC: 0.2425

## Official Combined ProtBERT + DNABERT-2 Model

Selected model:
SVM RBF

Test metrics:
- ROC-AUC: 0.7568
- PR-AUC: 0.7447
- F1: 0.6616
- MCC: 0.3435

## Best Overall Model After Phase 5

Best model:
5.3 | ProtBERT-SW + DNABERT-2 | SVM RBF

Metrics:
- ROC-AUC: 0.7568
- PR-AUC: 0.7447
- F1: 0.6616
- MCC: 0.3435

## Interpretation

If DNABERT-2 genomic-only outperforms K3/K4/Basic handcrafted genomic features, this suggests that genomic foundation embeddings capture regulatory sequence context beyond simple k-mer frequency patterns.

If DNABERT-2 does not outperform handcrafted genomic features, this remains a valid finding and may indicate that:
- the dataset is small,
- TSS-proximal sequences alone have limited signal,
- embedding extraction without fine-tuning is insufficient,
- handcrafted k-mer features are strong for this task,
- or the regulatory signal requires tissue-specific annotations.

If Combined ProtBERT + DNABERT-2 improves over Combined ProtBERT + K3/K4/Basic, then the genomic foundation model improves multimodal integration.

If not, the current handcrafted genomic branch remains the better practical representation for the framework.
