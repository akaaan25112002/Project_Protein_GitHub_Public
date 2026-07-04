
# Phase 4.1 — Biological Validation and Pathway Enrichment Report

## Objective

Phase 4.1 evaluated the biological plausibility of the official multimodal prediction results.

The analysis focused on gene lists produced by the official Phase 3 model:

- Combined Protein+Genomic SVM RBF
- Protein representation: ProtBERT sliding-window embedding
- Genomic representation: K3/K4/Basic TSS-proximal regulatory features

The main gene lists evaluated were:

- Top 50 combined predictions
- Top true positives
- Combined-rescued genes
- High-confidence false positives
- High-confidence false negatives
- Both-wrong genes

## Methods

Functional enrichment analysis was performed using g:Profiler through the `gprofiler-official` Python package.

The enrichment sources included:

- GO Biological Process
- GO Molecular Function
- GO Cellular Component
- KEGG
- Reactome
- WikiPathways
- Human Phenotype

In addition, a curated T2D-related gene set overlap analysis was performed using manually defined gene groups related to:

- known T2D/GWAS/monogenic diabetes genes
- insulin secretion and beta-cell function
- glucose metabolism and transport
- lipid metabolism and adipose biology
- mitochondrial oxidative phosphorylation
- inflammation and stress

## Enrichment Summary

Number of gene lists analyzed: 6

Number of gene lists with significant enrichment terms: 4

Number of gene lists with T2D-relevant keyword-matched terms: 2

Enrichment summary by gene list:

                 gene_list_name  n_input_genes  n_significant_terms  n_t2d_relevant_terms  best_p_value                                             top_term     top_t2d_relevant_term
             top_true_positives             86                  175                    63  6.968994e-11                          respiratory chain complex I oxidative phosphorylation
    top_50_combined_predictions             50                  102                    41  1.848562e-05             NADH dehydrogenase (ubiquinone) activity Oxidative phosphorylation
high_confidence_false_negatives             49                    3                     0  4.795541e-02                                     Anterior uveitis                      None
               both_wrong_genes             74                    1                     0  1.069641e-02 regulation of toll-like receptor 3 signaling pathway                      None
high_confidence_false_positives             40                    0                     0           NaN                                                 None                      None
         combined_rescued_genes             18                    0                     0           NaN                                                 None                      None

## Top 50 Curated T2D Support

Among the top 50 combined model predictions:

- Genes with curated T2D-related support: 15
- Percentage with curated support: 30.00%

Supported genes:

NDUFB2;NEUROD1;INSR;GAD1;NDUFV1;CACNA1D;HHEX;NDUFB3;SLC5A1;IGF2BP2;NDUFA7;SCD5;NDUFB1;DPP4;PDX1

## Top T2D-Relevant Enrichment Terms for Top 50 Predictions

source     native                                                                     name  p_value                      matched_biological_groups
  KEGG KEGG:00190                                                Oxidative phosphorylation 0.012901       mitochondria_energy;signaling_regulation
    WP   WP:WP623                                                Oxidative phosphorylation 0.014813       mitochondria_energy;signaling_regulation
 GO:BP GO:0006119                                                oxidative phosphorylation 0.030841       mitochondria_energy;signaling_regulation
 GO:BP GO:0031016                                                     pancreas development 0.049015 development_beta_cell;diabetes_glucose_insulin
 GO:MF GO:0008137                                 NADH dehydrogenase (ubiquinone) activity 0.000018                            mitochondria_energy
 GO:CC GO:0030964                                               NADH dehydrogenase complex 0.000021                            mitochondria_energy
 GO:CC GO:0045271                                              respiratory chain complex I 0.000021                            mitochondria_energy
 GO:BP GO:0006120                     mitochondrial electron transport, NADH to ubiquinone 0.000200                            mitochondria_energy
 GO:MF GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific 0.000291                           signaling_regulation
 GO:MF GO:0001216                             DNA-binding transcription activator activity 0.000326                           signaling_regulation

## Interpretation

The biological validation step evaluates whether the model's highest-ranked predictions are consistent with known diabetes-related biology.

A strong result would include enrichment or curated support for processes such as:

- insulin secretion
- glucose homeostasis
- pancreatic beta-cell function
- lipid metabolism
- mitochondrial metabolism
- inflammatory signaling
- PI3K-Akt / AMPK / PPAR signaling

The curated overlap analysis is not a replacement for full database validation, but it provides a useful first-pass biological plausibility check.

## Recommended Next Step

The next step is to inspect the enriched terms and top-supported genes manually, then write the final biological interpretation section.

Important gene groups to discuss include:

1. Top true positives with strong diabetes relevance
2. False positives with possible hidden or indirect diabetes relevance
3. Combined-rescued genes where genomic information improved prediction
4. Both-wrong genes that may indicate label noise or missing modalities
