
# Phase 8 — Expanded Biological Validation Report

## Objective

Phase 8 expanded the biological validation beyond the original top-50 analysis. The aim was to examine additional top-ranked genes, compare biological themes across protein-only, handcrafted multimodal, and DNABERT-2 multimodal models, and investigate how DNABERT-2 changes the top-ranked gene lists.

## Top-100 Biological Validation

The top-100 gene lists were extracted for three key models:

1. Protein-only ProtBERT-SW
2. Multimodal handcrafted: ProtBERT-SW + K3/K4/Basic
3. Multimodal DNABERT-2: ProtBERT-SW + DNABERT-2

## Enrichment Summary

Protein-only top 100:
- Significant terms: 106
- T2D-relevant terms: 29
- Top T2D-relevant term: NADH dehydrogenase (ubiquinone) activity

Handcrafted multimodal top 100:
- Significant terms: 103
- T2D-relevant terms: 27
- Top T2D-relevant term: NADH dehydrogenase complex

DNABERT-2 multimodal top 100:
- Significant terms: 74
- T2D-relevant terms: 25
- Top T2D-relevant term: NADH dehydrogenase complex

## DNABERT-2 Movement Analysis

Between handcrafted multimodal and DNABERT-2 multimodal top-100 lists:

- Shared top-100 genes: 87
- DNABERT-2 moved-in genes: 13
- Handcrafted moved-out genes: 13
- Jaccard overlap: 0.7699

This analysis helps explain whether DNABERT-2 improves ranking by preserving the same biological candidates or by shifting toward a different biological signal.

## Interpretation

If the handcrafted multimodal top-100 list shows stronger oxidative phosphorylation, mitochondrial, insulin, glucose, beta-cell, or pancreatic development support, this reinforces its role as the official biologically validated model.

If DNABERT-2 moved-in genes show different biological themes, this supports the interpretation that DNABERT-2 captures different regulatory sequence signals. This may explain why DNABERT-2 improves ROC-AUC while showing weaker enrichment in the original top-50 validation.

## Output

Phase 8 generated:

- Top-100 ranked gene tables
- Curated biological theme overlap tables
- DNABERT-2 moved-in and moved-out gene tables
- Expanded g:Profiler enrichment results
- Candidate literature evidence seed table
- Theme overlap figures
- Enrichment summary figures
