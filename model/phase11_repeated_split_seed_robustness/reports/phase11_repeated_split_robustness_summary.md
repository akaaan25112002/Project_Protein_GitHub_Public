
# Phase 11 — Repeated-Split / Multi-Seed Robustness Evaluation

## Objective

Phase 11 addressed the main statistical vulnerability identified in the supervisor feedback: the previous comparison relied on a single held-out test split. Although bootstrap confidence intervals estimate uncertainty within that test set, they do not capture variation across different train/test splits or random seeds. Therefore, this phase repeated the evaluation across multiple stratified splits.

## Experimental Design

Number of repeated seeds: 10

Seeds used:
[11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

Split ratio:
- Train: 0.70
- Validation: 0.15
- Test: 0.15

Models evaluated:
1. Protein-only ProtBERT-SW
2. Genomic-only K3/K4/Basic
3. Multimodal handcrafted: ProtBERT-SW + K3/K4/Basic
4. Multimodal DNABERT-2: ProtBERT-SW + DNABERT-2

Primary ranking metric:
- PR-AUC

Primary threshold-dependent metric:
- MCC

Secondary metrics:
- ROC-AUC
- F1

Thresholds for classification metrics were selected on the validation set using MCC, then evaluated on the test set.

## Main Results

Best mean PR-AUC model:
- Multimodal_DNABERT2
- PR-AUC mean = 0.7256
- PR-AUC SD = 0.0347

Best mean MCC model:
- Multimodal_DNABERT2
- MCC mean = 0.3522
- MCC SD = 0.0728

Best mean ROC-AUC model:
- Multimodal_DNABERT2
- ROC-AUC mean = 0.7454
- ROC-AUC SD = 0.0304

## Interpretation

This repeated-split analysis should be used to determine whether the single-test-set conclusions remain stable. If DNABERT-2 remains the highest ROC-AUC model across repeated splits, the interpretation can be that DNABERT-2 provides a small but more robust global-ranking gain. However, if the ranking changes across seeds, the language should be softened further and the main manuscript story should emphasize the ranking-versus-interpretability trade-off rather than model superiority.

## Reviewer-Relevant Contribution

This phase directly addresses the concern that model rankings may depend on a single train/test split. Reporting mean ± SD across repeated seeds makes the statistical evidence more publication-ready and reduces the vulnerability of relying only on bootstrap confidence intervals from one held-out test set.
