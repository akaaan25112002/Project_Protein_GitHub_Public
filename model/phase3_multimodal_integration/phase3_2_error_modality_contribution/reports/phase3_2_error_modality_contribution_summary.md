
# Phase 3.2 — Multimodal Error and Modality Contribution Analysis

## Objective

Phase 3.2 analyzed the official multimodal integration result from Phase 3.1.

The analysis focused on:

1. Error comparison between Protein-only SVM and Combined Protein+Genomic SVM.
2. Block permutation importance for protein and genomic feature blocks.
3. Supplementary Logistic Regression coefficient analysis for modality contribution.

## Models Compared

Protein-only model:
- ProtBERT sliding-window embeddings
- SVM RBF
- Threshold: 0.5

Combined model:
- ProtBERT sliding-window embeddings + K3/K4/Basic genomic features
- SVM RBF
- Threshold: 0.5

## Test Performance Comparison

Protein-only SVM:
- ROC-AUC: 0.7274
- PR-AUC: 0.7433
- F1: 0.6667
- MCC: 0.3215

Combined SVM:
- ROC-AUC: 0.7290
- PR-AUC: 0.7573
- F1: 0.6590
- MCC: 0.3438

## Error Group Analysis

Number of test genes: 271

- Both correct: 164
- Both wrong: 74
- Combined correct, protein wrong: 18
- Protein correct, combined wrong: 15

The 'combined correct, protein wrong' group represents genes rescued by multimodal integration.
The 'protein correct, combined wrong' group represents genes where integration reduced classification correctness.

## Block Permutation Importance

Baseline Combined SVM:
- ROC-AUC: 0.7290
- PR-AUC: 0.7573
- F1: 0.6590
- MCC: 0.3438

Protein block permutation:
- Mean ROC-AUC drop: 0.1989
- Mean PR-AUC drop: 0.2243
- Mean F1 drop: 0.1477
- Mean MCC drop: 0.3084

Genomic block permutation:
- Mean ROC-AUC drop: 0.0221
- Mean PR-AUC drop: 0.0394
- Mean F1 drop: 0.0074
- Mean MCC drop: 0.0292

Interpretation:
- A larger drop after permuting a block indicates stronger dependence on that modality.
- If both protein and genomic block permutation reduce performance, the combined model uses both modalities.
- If only protein permutation strongly reduces performance, the combined model is mostly protein-driven.


## Interpretable Logistic Regression Coefficient Analysis

A supplementary Combined Logistic Regression model was used for interpretability.

Modality coefficient summary:

modality  n_features  sum_abs_coefficient  mean_abs_coefficient  median_abs_coefficient  max_abs_coefficient  share_of_total_abs_coefficient
 genomic         355             2.773525              0.007813                0.006411             0.036489                        0.295401
 protein        1024             6.615487              0.006460                0.005430             0.031693                        0.704599

This analysis is supplementary and does not replace the official Combined SVM model.


## Conclusion

Phase 3.2 provides interpretability evidence for the multimodal result.

The key question is whether the combined model improves ranking and whether the genomic block contributes beyond protein embeddings.

This analysis should be used to support the final Phase 3 report and decide whether further integration methods such as PCA integration, late fusion, or DNABERT embeddings are needed.
