
# Phase 2.0 — Genomic Regulatory Dataset QC and Split Summary

## Dataset

The genomic regulatory dataset used in Phase 2 is:

t2d_tss_proximal_regulatory_sequences_2kbup_500bpdown_nuclear_balanced_v1.csv

This dataset contains TSS-proximal regulatory DNA sequences defined as:

2,000 bp upstream + 500 bp downstream of the transcription start site (TSS)

Total window length: 2,500 bp per gene.

## Dataset Size

Total genes: 1806
Negative/background genes: 903
Positive/T2D-associated genes: 903

The dataset is balanced with a 1:1 positive-to-negative ratio.

## Sequence Quality

Detected sequence column: tss_proximal_sequence

All sequences were standardized into the column:

regulatory_sequence

Sequence length:
- Minimum: 2500
- Median: 2500.0
- Mean: 2500.0
- Maximum: 2500

Invalid DNA character rows: 0
Total N bases: 0

## Split Strategy

The dataset was split using stratified sampling:

- Train: 70%
- Validation: 15%
- Test: 15%
- random_state = 42

## Split Summary

     split    n  n_negative  n_positive  positive_ratio  min_sequence_length  median_sequence_length  mean_sequence_length  max_sequence_length  total_N_bases
     train 1264         632         632        0.500000                 2500                  2500.0                2500.0                 2500              0
validation  271         135         136        0.501845                 2500                  2500.0                2500.0                 2500              0
      test  271         136         135        0.498155                 2500                  2500.0                2500.0                 2500              0

## Leakage Checks

No gene_id overlap was found across train, validation, and test splits.
No regulatory sequence overlap was found across train, validation, and test splits.

## Output Files

Train split:
/content/drive/MyDrive/Project_Protein/model/phase2_genomic_regulatory_baseline/splits/train_genomic_regulatory_v1.csv

Validation split:
/content/drive/MyDrive/Project_Protein/model/phase2_genomic_regulatory_baseline/splits/val_genomic_regulatory_v1.csv

Test split:
/content/drive/MyDrive/Project_Protein/model/phase2_genomic_regulatory_baseline/splits/test_genomic_regulatory_v1.csv

## Next Step

The next step is Phase 2.1: Genomic handcrafted feature extraction.

Recommended baseline features:
- GC content
- AT content
- CpG count and CpG observed/expected ratio
- AT skew and GC skew
- k-mer frequencies for k = 3 and k = 4
- Optional k = 5 feature set for ablation
