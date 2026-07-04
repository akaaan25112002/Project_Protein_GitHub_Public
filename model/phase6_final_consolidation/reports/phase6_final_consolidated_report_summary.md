
# Final Consolidated Report Summary — Phase 1 to Phase 6

## Final Model Decision

This project evaluated protein sequence representations, genomic regulatory sequence features, multimodal integration, biological validation, and a DNABERT-2 genomic foundation-model extension for Type 2 Diabetes-associated gene/protein prediction.

The final model decision separates two roles:

1. Official biologically validated model
2. Best ROC-AUC extension model

## Official Biologically Validated Model

The official biologically validated model is:

Combined ProtBERT-SW + K3/K4/Basic SVM RBF

This model achieved:

- ROC-AUC: 0.7290
- PR-AUC: 0.7573
- F1: 0.6590
- MCC: 0.3438

It is retained as the main biologically validated model because its top-ranked predictions showed the strongest biological enrichment and curated T2D-related support.

Specifically, the top 50 predictions produced:

- 102 significant enrichment terms
- 41 T2D-relevant enrichment terms
- 15/50 genes with curated T2D-related support

The enriched terms included oxidative phosphorylation, respiratory chain complex I, insulin resistance, type II diabetes mellitus, insulin secretion, and pancreas development.

## Best ROC-AUC Extension Model

The best ROC-AUC model is:

Combined ProtBERT-SW + DNABERT-2 SVM RBF

This model achieved:

- ROC-AUC: 0.7568
- PR-AUC: 0.7447
- F1: 0.6642
- MCC: 0.3433

Compared with the Phase 3.1 handcrafted-genomic multimodal model, the DNABERT-2 extension improved ROC-AUC by +0.0278. This suggests that DNABERT-2 genomic embeddings improve global ranking separation and capture useful regulatory sequence context beyond handcrafted k-mer features.

However, the DNABERT-2 extension did not fully replace the handcrafted genomic branch. The Phase 3.1 model retained higher PR-AUC, slightly higher MCC, and stronger biological validation among top-ranked genes.

## Final Interpretation

Protein foundation embeddings provide the dominant disease-association signal in this project. Genomic regulatory features provide complementary information, especially when integrated with protein embeddings. Handcrafted K3/K4/Basic TSS-proximal features produced the strongest biological validation, while DNABERT-2 embeddings improved ROC-AUC as a genomic foundation-model extension.

Therefore, the final conclusion is:

The proposed framework demonstrates that protein foundation embeddings are highly informative for T2D gene/protein association prediction, while genomic regulatory features add complementary biological context. DNABERT-2 further improves global ranking performance, supporting the value of genomic foundation models, but additional fine-tuning and biological validation are needed before replacing the handcrafted genomic branch as the main biologically validated model.

## Recommended Report Framing

The final report should present:

- Phase 3.1 as the official biologically validated multimodal model.
- Phase 5.3 as the best ROC-AUC DNABERT-2 extension.
- Phase 6 as the final consolidation proving that both handcrafted genomic features and genomic foundation embeddings have value.

## Final Claim

Protein embeddings are the main predictive signal, TSS-proximal genomic features add complementary biological information, and DNABERT-2 provides a promising extension that improves ROC-AUC but requires stronger biological validation and/or fine-tuning for future work.
