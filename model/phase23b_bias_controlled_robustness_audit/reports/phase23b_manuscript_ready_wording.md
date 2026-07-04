## Methods - Bias-Controlled Robustness Audit

Following the leakage and bias audit, an additional bias-controlled robustness analysis was performed to isolate the contribution of metadata and nuisance signals. Nuisance-only classifiers were evaluated using separate feature sets: all nuisance variables, pure feature-summary variables excluding gene-symbol length, protein-summary variables, genomic-summary variables and gene-symbol length alone. Because gene-symbol length showed strong positive-negative imbalance but was not used by the main sequence models, a matched-sampling stress test was also performed. Positives and negatives were matched within gene-symbol-length bins, and the main protein-only and multimodal models were re-evaluated using repeated cross-validation on the matched subsets.

## Results - Metadata and Nuisance Bias Controls

The nuisance-only analysis showed that all nuisance variables achieved PR-AUC 0.627, while pure feature-summary variables excluding gene-symbol length achieved PR-AUC 0.626. Gene-symbol length alone achieved PR-AUC 0.499, confirming that this metadata artifact carried some label information but was not directly used by the main models. Under gene-symbol-length-matched sampling, the strongest PR-AUC was obtained by Early_fusion_Protein_DNABERT2 (0.722), indicating whether the main ranking signal persisted after balancing the strongest observed metadata artifact.

## Discussion - Dataset Bias Interpretation

This bias-controlled audit clarifies the interpretation of the Phase 23 findings. A significant gene-symbol-length difference indicates annotation-source imbalance between positive and negative sets, but this variable was not part of the model input features. Therefore, it should be reported as a dataset-level bias rather than direct model leakage. If pure feature-summary nuisance performance remains much lower than the main models and matched-sampling performance remains similar to the original repeated-CV results, the framework can be described as moderately robust with explicit bias controls. If matched performance drops substantially, the claims should be further softened and framed as sequence-based prioritization under known dataset construction bias.

