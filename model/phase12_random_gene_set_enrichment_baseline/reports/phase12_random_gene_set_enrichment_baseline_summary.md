# Phase 12 — Random-Gene-Set Biological Enrichment Baseline

## Objective

Phase 12 addressed the reviewer-relevant concern that the observed biological enrichment in top-ranked genes may arise by chance due to list size or candidate-universe composition. To test this, observed model top-50 and top-100 gene lists were compared against random gene sets of the same size sampled from the same candidate universe.

## Experimental Design

- Candidate universe size: 271 genes.
- Number of random permutations: 1000.
- Top-N list sizes tested: [50, 100].
- Random seed: 42.
- Empirical p-value: proportion of random sets with theme count greater than or equal to the observed model count.
- Multiple comparison correction: Benjamini-Hochberg FDR.

## Key Results: Main Top-100 Biological Themes

### Protein_only_ProtBERT_SW
- Protein_only_ProtBERT_SW top100 mitochondrial_function: observed=8, random mean=3.69 ± 1.52, enrichment ratio=2.17, empirical p=0.0060, FDR p=0.0640.
- Protein_only_ProtBERT_SW top100 oxidative_phosphorylation: observed=8, random mean=3.69 ± 1.52, enrichment ratio=2.17, empirical p=0.0060, FDR p=0.0640.
- Protein_only_ProtBERT_SW top100 known_t2d_gwas_or_monogenic: observed=10, random mean=5.24 ± 1.77, enrichment ratio=1.91, empirical p=0.0100, FDR p=0.0640.
- Protein_only_ProtBERT_SW top100 beta_cell_biology: observed=7, random mean=3.41 ± 1.40, enrichment ratio=2.05, empirical p=0.0190, FDR p=0.0791.
- Protein_only_ProtBERT_SW top100 glucose_metabolism: observed=2, random mean=1.12 ± 0.87, enrichment ratio=1.78, empirical p=0.3197, FDR p=0.4654.
- Protein_only_ProtBERT_SW top100 insulin_signalling: observed=1, random mean=0.35 ± 0.48, enrichment ratio=2.83, empirical p=0.3536, FDR p=0.4654.
- Protein_only_ProtBERT_SW top100 pancreatic_development: observed=3, random mean=1.49 ± 0.96, enrichment ratio=2.02, empirical p=0.1499, FDR p=0.3058.

### Multimodal_handcrafted
- Multimodal_handcrafted top100 mitochondrial_function: observed=7, random mean=3.69 ± 1.52, enrichment ratio=1.90, empirical p=0.0380, FDR p=0.1158.
- Multimodal_handcrafted top100 oxidative_phosphorylation: observed=7, random mean=3.69 ± 1.52, enrichment ratio=1.90, empirical p=0.0380, FDR p=0.1158.
- Multimodal_handcrafted top100 known_t2d_gwas_or_monogenic: observed=10, random mean=5.24 ± 1.77, enrichment ratio=1.91, empirical p=0.0100, FDR p=0.0640.
- Multimodal_handcrafted top100 beta_cell_biology: observed=7, random mean=3.41 ± 1.40, enrichment ratio=2.05, empirical p=0.0190, FDR p=0.0791.
- Multimodal_handcrafted top100 glucose_metabolism: observed=2, random mean=1.12 ± 0.87, enrichment ratio=1.78, empirical p=0.3197, FDR p=0.4654.
- Multimodal_handcrafted top100 insulin_signalling: observed=1, random mean=0.35 ± 0.48, enrichment ratio=2.83, empirical p=0.3536, FDR p=0.4654.
- Multimodal_handcrafted top100 pancreatic_development: observed=3, random mean=1.49 ± 0.96, enrichment ratio=2.02, empirical p=0.1499, FDR p=0.3058.

### Multimodal_DNABERT2
- Multimodal_DNABERT2 top100 mitochondrial_function: observed=6, random mean=3.69 ± 1.52, enrichment ratio=1.62, empirical p=0.1299, FDR p=0.3058.
- Multimodal_DNABERT2 top100 oxidative_phosphorylation: observed=6, random mean=3.69 ± 1.52, enrichment ratio=1.62, empirical p=0.1299, FDR p=0.3058.
- Multimodal_DNABERT2 top100 known_t2d_gwas_or_monogenic: observed=10, random mean=5.24 ± 1.77, enrichment ratio=1.91, empirical p=0.0100, FDR p=0.0640.
- Multimodal_DNABERT2 top100 beta_cell_biology: observed=7, random mean=3.41 ± 1.40, enrichment ratio=2.05, empirical p=0.0190, FDR p=0.0791.
- Multimodal_DNABERT2 top100 glucose_metabolism: observed=2, random mean=1.12 ± 0.87, enrichment ratio=1.78, empirical p=0.3197, FDR p=0.4654.
- Multimodal_DNABERT2 top100 insulin_signalling: observed=1, random mean=0.35 ± 0.48, enrichment ratio=2.83, empirical p=0.3536, FDR p=0.4654.
- Multimodal_DNABERT2 top100 pancreatic_development: observed=3, random mean=1.49 ± 0.96, enrichment ratio=2.02, empirical p=0.1499, FDR p=0.3058.

## Handcrafted vs DNABERT-2 Interpretation

This random baseline should be used to determine whether the stronger biological interpretation of the handcrafted multimodal model is supported beyond random expectation. If handcrafted top-ranked genes show higher mitochondrial/OXPHOS enrichment ratios or lower empirical p-values than DNABERT-2, this supports the ranking-versus-interpretability trade-off: DNABERT-2 improves global ranking while handcrafted genomic features preserve more pathway-specific biological concentration.

## Reviewer-Relevant Contribution

This phase directly addresses the concern that enrichment may be an artefact of random list composition. By sampling same-size random gene sets from the same candidate universe, the analysis provides an empirical baseline for evaluating whether observed OXPHOS, mitochondrial, beta-cell, glucose, and known T2D theme concentrations are stronger than expected by chance.