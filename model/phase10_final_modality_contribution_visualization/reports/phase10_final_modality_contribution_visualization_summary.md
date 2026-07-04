
# Phase 10 — Final Modality Contribution and Visualization Package

## Objective

Phase 10 consolidated the final evidence package and analysed how protein and genomic representations contribute to model behaviour. This phase focused on modality contribution, score/rank shifts, rescued and lost genes, and final visualization outputs.

## Final Performance Summary

Protein-only ProtBERT-SW:
- ROC-AUC = 0.7274
- PR-AUC = 0.7433
- MCC = 0.3215

Genomic-only K3/K4/Basic:
- ROC-AUC = 0.6397
- PR-AUC = 0.6215
- MCC = 0.1372

Handcrafted multimodal:
- ROC-AUC = 0.7290
- PR-AUC = 0.7573
- MCC = 0.3438

DNABERT-2 multimodal:
- ROC-AUC = 0.7568
- PR-AUC = 0.7447
- MCC = 0.3433

## Modality Contribution

Protein embeddings are the dominant predictive signal because the protein-only model remains close to multimodal performance. Genomic-only features are weaker as a standalone predictor, but multimodal models show that genomic information changes score/rank behaviour, error patterns, and biological enrichment.

## Rescued and Lost Genes

Compared with protein-only:

Handcrafted multimodal:
- Rescued genes: 18
- Lost genes: 15

DNABERT-2 multimodal:
- Rescued genes: 23
- Lost genes: 20

These rescued/lost genes are useful for explaining which candidates benefit from adding genomic representations.

## DNABERT-2 Behaviour

Phase 9 showed that DNABERT-2 improves global ranking but weakens biological enrichment because moved-in genes do not form a strong T2D-relevant biological cluster, while moved-out genes include mitochondrial/OXPHOS, glucose metabolism, and known T2D genes.

## Final Positioning

The official biologically validated model remains the handcrafted multimodal model:
- ProtBERT-SW protein embedding + K3/K4/Basic genomic regulatory features.

The best ROC-AUC extension is:
- ProtBERT-SW protein embedding + DNABERT-2 genomic embedding.

The overall framework can be described as:
- protein-dominant,
- genomically supported,
- statistically evaluated,
- biologically validated,
- and extensible to genomic foundation models.

## Figures Generated

Phase 10 generated final figures for:
- ROC comparison
- PR comparison
- metric comparison
- ROC-AUC/PR-AUC confidence intervals
- score shift by label
- rescued/lost genes
- biological themes in rescued/lost genes
- DNABERT-2 top-list movement
- enrichment summary
- top-100 biological theme comparison
