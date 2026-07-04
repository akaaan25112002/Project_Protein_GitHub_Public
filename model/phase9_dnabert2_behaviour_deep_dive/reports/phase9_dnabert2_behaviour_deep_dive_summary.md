
# Phase 9 — DNABERT-2 Behaviour Deep Dive Report

## Objective

Phase 9 investigated why the DNABERT-2 multimodal model achieved the highest ROC-AUC but showed weaker biological enrichment than the handcrafted multimodal model. The analysis focused on rank shifts, score shifts, moved-in/moved-out genes, biological theme changes, and enrichment differences.

## Top-List Stability

Top-50 comparison:
- Shared genes: 39
- DNABERT-2 moved-in genes: 11
- Handcrafted moved-out genes: 11
- Jaccard overlap: 0.6393

Top-100 comparison:
- Shared genes: 87
- DNABERT-2 moved-in genes: 13
- Handcrafted moved-out genes: 13
- Jaccard overlap: 0.7699

The top-100 list is more stable than the top-50 list, suggesting that DNABERT-2 does not completely change the candidate space but changes the ordering of the highest-ranked genes.

## Enrichment Behaviour

Handcrafted multimodal top100:
- Significant terms: 103
- T2D-relevant terms: 27
- Top relevant term: NADH dehydrogenase complex

DNABERT-2 multimodal top100:
- Significant terms: 74
- T2D-relevant terms: 25
- Top relevant term: NADH dehydrogenase complex

DNABERT-2 moved-in top100:
- Significant terms: 0
- T2D-relevant terms: 0

DNABERT-2 moved-out top100:
- Significant terms: 2
- T2D-relevant terms: 2
- Top relevant term: NADH dehydrogenase complex

## Interpretation

DNABERT-2 improves global ranking performance, but its moved-in genes do not form a strong enriched T2D-related biological cluster. In contrast, several genes moved out of the handcrafted top-ranked list belong to mitochondrial function, oxidative phosphorylation, glucose metabolism, or known T2D biology. This explains why DNABERT-2 can improve ROC-AUC while showing weaker biological enrichment.

## Main Conclusion

DNABERT-2 captures useful ranking information across the full test set, which explains its higher ROC-AUC. However, the handcrafted genomic features preserve a more concentrated mitochondrial/OXPHOS and curated T2D biological signal among the highest-ranked genes. Therefore, DNABERT-2 should be interpreted as a statistically useful ranking extension, while the handcrafted multimodal model remains the stronger biologically interpretable model.
