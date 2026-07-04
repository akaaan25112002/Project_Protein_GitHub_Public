
# Phase 2.3 — Cross-Modality Error Comparison Summary

## Objective

This analysis compared protein-based and genomic regulatory-based predictions on the overlapping test genes.

The goal was to determine whether protein sequence and TSS-proximal regulatory DNA models make complementary errors.

## Models Compared

Protein model:
- ProtBERT sliding-window + Logistic Regression
- Protein score threshold policy: protein_pred_tuned_f1

Genomic model:
- K3 + K4 + Basic genomic features + Random Forest
- Genomic score threshold policy: genomic_pred_default_0_5

## Overlapping Test Set

Number of overlapping genes: 45

Label counts:
true_label
0    26
1    19

## Cross-Modality Error Groups

- Both correct: 15
- Both wrong: 10
- Protein correct, genomic wrong: 10
- Genomic correct, protein wrong: 10

## Interpretation

If the protein-only-correct and genomic-only-correct groups are substantial, this indicates that the two modalities capture complementary biological signals.

Protein sequence may capture coding/protein-level information, while TSS-proximal regulatory DNA captures promoter/regulatory sequence patterns.

This provides direct justification for Phase 3 multimodal integration.

## Diagnostic Simple Fusion

A simple mean score fusion was tested only as an exploratory diagnostic.

Default fusion metrics:
                               model  n  accuracy  precision  recall_sensitivity  specificity       f1  roc_auc   pr_auc      mcc  tn  fp  fn  tp
Simple mean fusion score default 0.5 45  0.666667   0.590909            0.684211     0.653846 0.634146 0.690283 0.634041 0.334024  17   9   6  13

This is not considered the final integration model because it was evaluated on the overlapping test subset without a separate validation protocol.

## Next Step

Proceed to Phase 3 multimodal integration using a shared gene split and features from both modalities.

Recommended Phase 3 input:
- ProtBERT sliding-window protein embeddings
- K3 + K4 + Basic genomic regulatory features

Recommended model families:
- Logistic Regression
- SVM RBF
- Random Forest
- LightGBM
- Soft Voting
- Stacking
