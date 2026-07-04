
# Phase 5.4B — DNABERT-2 Extension Biological Quick Validation Report

## Objective

Phase 5.4B evaluated whether the new best ROC-AUC model, Combined ProtBERT-SW + DNABERT-2 SVM RBF, produces biologically plausible top-ranked genes and whether it should replace or extend the previous biologically validated multimodal model.

## Model Performance

The Phase 5.3 model achieved:

- ROC-AUC: 0.7568
- PR-AUC: 0.7447
- F1: 0.6642
- MCC: 0.3433

Compared with the previous Phase 3.1 multimodal model:

- ROC-AUC delta: +0.0278
- PR-AUC delta: -0.0126
- F1 delta: +0.0052
- MCC delta: -0.0005

This indicates that DNABERT-2 improves global ranking separation measured by ROC-AUC, while the previous handcrafted-genomic multimodal model remains competitive in PR-AUC and MCC.

## Top 50 Gene Comparison

Top 50 overlap between Phase 5 and Phase 3:

- Shared top 50 genes: 39
- New Phase 5-only top 50 genes: 11
- Jaccard overlap: 0.6393

This measures whether DNABERT-2 changes the biological candidate ranking or mostly preserves the previous candidate set.

## Curated Biological Support

Among the Phase 5 top 50 genes:

- Genes with curated T2D-related support: 10/50
- Percentage with support: 20.00%

Supported top-ranked genes:

CACNA1D;GAD1;INSR;NDUFV1;NDUFB2;HHEX;SCD5;NEUROD1;PDX1;IGF2BP2

## Enrichment Summary

For Phase 5 top 50 predictions:

- Significant enrichment terms: 43
- T2D-relevant enrichment terms: 16

## Interpretation

If the Phase 5 top 50 genes retain diabetes-relevant enrichment and curated support, then the DNABERT-2 extension can be reported as a stronger genomic foundation-model extension.

If biological support is weaker than Phase 3, then Phase 5 should be reported as an ROC-AUC-improving extension, while Phase 3 remains the main biologically validated model.

Recommended interpretation:

- Phase 5 improves ROC-AUC.
- DNABERT-2 genomic embeddings outperform handcrafted genomic features in ranking metrics.
- Combined ProtBERT-SW + DNABERT-2 is the best ROC-AUC model.
- The previous Combined ProtBERT-SW + K3/K4/Basic model remains highly competitive and already has full biological validation.
