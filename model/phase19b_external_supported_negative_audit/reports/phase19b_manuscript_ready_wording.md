## Methods - Label-Contamination-Aware External Audit

Because disease-gene labels are incomplete, an additional label-contamination-aware audit was performed after external gene-set validation. External-supported genes that were labelled negative in the current dataset were identified and ranked using out-of-fold model scores. The analysis tested whether these external-supported current negatives received higher model scores than ordinary negatives, and whether top-ranked negative-labelled genes were enriched for external evidence compared with random negative-gene baselines. This audit was used to distinguish likely background negatives from potential unknown positives or annotation-incomplete candidates.

## Results - External-Supported Current Negatives

External gene-set validation did not show strong global enrichment after multiple-testing correction. However, the label audit identified several current-negative genes with independent external support and relatively high model ranks. High-priority candidates included NDUFV1, NDUFA12, GIPR, NDUFB10, MTNR1B, NDUFS7, NDUFA9, NDUFB4. These genes should not be interpreted as ordinary false positives. Instead, they represent possible unknown positives, annotation-incomplete genes or pathway-level candidates that expose the limitations of binary disease-gene labelling.

## Discussion - Incomplete Negative Labels

The external-supported negative audit changes the interpretation of weak external validation. Rather than treating all negative-labelled external genes as model errors, the results indicate that the negative class contains biologically plausible genes with independent support. This is expected in disease-gene prioritization, where the absence of curated disease evidence does not guarantee true non-association. Therefore, model performance should be interpreted as ranking utility under incomplete labels rather than definitive disease/non-disease classification. This strengthens the manuscript by explicitly addressing negative-label uncertainty and by identifying relabel or follow-up candidates for future validation.

