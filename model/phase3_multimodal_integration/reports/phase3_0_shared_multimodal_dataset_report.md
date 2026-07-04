
# Phase 3.0 — Shared Multimodal Dataset Preparation

## Objective

The purpose of Phase 3.0 was to create a shared multimodal dataset for protein + genomic integration.

The two modalities are:

1. Protein sequence representation:
   ProtBERT sliding-window embeddings

2. Genomic regulatory representation:
   K3 + K4 + Basic TSS-proximal handcrafted genomic features

## Input Sources

Protein source:
/content/drive/MyDrive/Project_Protein/model/phase1_2_protbert_sliding_window_embedding/embeddings

Genomic source:
/content/drive/MyDrive/Project_Protein/model/phase2_genomic_regulatory_baseline/features

## Shared Gene Set

Protein genes available: 1820
Genomic genes available: 1806
Shared multimodal genes: 1806

Label distribution in shared set:
label
0    903
1    903

## Feature Dimensions

Protein features: 1024
Genomic features: 356
Combined features: 1380

## Shared Split Strategy

The shared multimodal dataset was split using:

- 70% train
- 15% validation
- 15% test
- stratified by label
- random_state = 42

## Split Summary

     split    n  n_negative  n_positive  positive_ratio  n_protein_features  n_genomic_features  n_combined_features  unique_gene_id
     train 1264         632         632        0.500000                1024                 356                 1380            1264
validation  271         135         136        0.501845                1024                 356                 1380             271
      test  271         136         135        0.498155                1024                 356                 1380             271

## Leakage Check

No gene_id overlap was found across train, validation, and test splits.

## Output Files

Metadata:
- train_multimodal_metadata_v1.csv
- val_multimodal_metadata_v1.csv
- test_multimodal_metadata_v1.csv

Protein features:
- X_train_protein_protbert_sw_v1.npy
- X_val_protein_protbert_sw_v1.npy
- X_test_protein_protbert_sw_v1.npy

Genomic features:
- X_train_genomic_k3k4basic_v1.csv
- X_val_genomic_k3k4basic_v1.csv
- X_test_genomic_k3k4basic_v1.csv

Combined features:
- X_train_combined_protein_genomic_v1.npy
- X_val_combined_protein_genomic_v1.npy
- X_test_combined_protein_genomic_v1.npy

## Next Step

The next step is Phase 3.1: train and evaluate multimodal integration models.

Recommended models:
- Logistic Regression
- SVM RBF
- Random Forest
- LightGBM
- Soft Voting
- Stacking

Recommended comparison:
- protein-only on shared split
- genomic-only on shared split
- combined protein + genomic on shared split
