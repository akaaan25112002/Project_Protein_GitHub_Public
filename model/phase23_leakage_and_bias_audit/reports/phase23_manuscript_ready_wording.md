## Methods - Leakage and Bias Audit

A leakage and bias audit was performed to evaluate whether model performance could be inflated by duplicated samples, feature-row duplication, train-test near-neighbor similarity or nuisance-variable confounding. Duplicate gene symbols and rounded duplicate feature vectors were identified across the full candidate set. For the original held-out split, each test protein embedding was compared with all train/validation embeddings using cosine similarity to identify potential near-duplicate leakage. Nuisance variables, including embedding norms, feature means, feature standard deviations, zero-vector fractions and available sequence-length proxies, were compared between positive and negative labels. A nuisance-only classifier was also evaluated to test whether simple non-biological artifacts alone could predict labels. Finally, protein-embedding clusters were used to create a group-aware split stress test as a surrogate for homology-aware evaluation.

## Results - Leakage and Bias Audit

The leakage audit found a maximum train/validation-to-test protein-embedding cosine similarity of 0.9950. The number of test samples in the very-high possible-duplicate category was 0, and the number in the high near-duplicate category was 1. The nuisance-only classifier achieved PR-AUC 0.627 and ROC-AUC 0.633, providing a direct estimate of how much label information could be recovered from simple feature-summary variables alone. Protein-embedding cluster-aware cross-validation produced an average PR-AUC change of -0.020 relative to random cross-validation across audited feature sets.

## Discussion - Robustness and Bias Interpretation

The leakage and bias audit should be used as a robustness and limitation layer. If duplicate or near-duplicate samples are rare and nuisance-only performance is close to random, this supports the interpretation that the main models are not primarily driven by trivial artifacts. If cluster-aware performance drops substantially relative to random cross-validation, the results should be interpreted more cautiously because part of the signal may reflect protein-family or embedding-neighborhood similarity. In either case, reporting this audit strengthens the manuscript by explicitly addressing common reviewer concerns in disease-gene prioritization studies.

