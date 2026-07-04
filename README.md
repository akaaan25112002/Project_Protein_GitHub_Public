# Project Protein: Bias-Audited Multimodal Sequence-Based Framework for T2D Gene/Protein Prioritization

## Overview

This repository contains the public supporting files for a gene/protein-level Type 2 Diabetes (T2D) candidate prioritization project.

The study evaluates whether sequence-derived protein and genomic representations can support T2D candidate gene/protein prioritization under a controlled and bias-audited machine learning framework.

This repository is organized according to the original phase-based project workflow. Each phase folder contains the corresponding code/notebooks, processed outputs, model artifacts, evaluation tables, figures, and summary files for that stage of the analysis.

## Important scope clarification

This project is **not** a patient-level T2D diagnosis model.

The task is:

> gene/protein-level candidate prioritization for T2D-relevant biological mechanisms.

The labels and model outputs should not be interpreted as clinical diagnostic predictions, patient risk scores, or causal proof of T2D association.

## Repository structure

```text
Project_Protein_GitHub_Public/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── DATA_LICENSE_NOTICE.md
├── .gitignore
├── requirements.txt
├── environment.yml
│
├── manuscript/
│   ├── main.tex
│   ├── references.bib
│   └── manuscript_final.pdf
│
├── graphical_abstract/
│   ├── graphical_abstract.png
│   └── graphical_abstract_source.pptx
│
├── data/
│   ├── README_dataset.md
│   ├── data_dictionary.csv
│   ├── processed_dataset.csv
│   ├── positive_gene_sources.csv
│   ├── background_gene_sources.csv
│   └── splits/
│
├── model/
│   ├── phase01_...
│   ├── phase02_...
│   ├── ...
│   ├── phase22_multimodal_fusion_strategy_comparison/
│   ├── phase23_leakage_and_bias_audit/
│   ├── phase23b_bias_controlled_robustness_audit/
│   ├── phase24_topk_ranking_utility_metrics/
│   └── phase25_final_manuscript_results_integration/
│
├── figures/
│   ├── fig1_pipeline.png
│   ├── fig2_model_performance.png
│   ├── fig3_fusion_comparison.png
│   ├── fig4_bias_audit.png
│   ├── fig5_topk_ranking.png
│   └── fig6_candidate_gene_pathway_heatmap.png
│
└── results/
    └── final_report_tables/
```

## Main analysis components

The project includes:

1. Dataset construction and sequence cleaning.
2. Protein baseline modelling.
3. Genomic regulatory feature construction.
4. Protein embedding extraction.
5. Multimodal dataset construction.
6. Repeated cross-validation benchmarking.
7. Fusion strategy comparison.
8. Leakage and bias auditing.
9. Bias-controlled robustness checks.
10. Top-K ranking utility analysis.
11. Literature-supported biological validation.
12. Final manuscript integration.

## Key final phases

The manuscript primarily uses outputs from the following final phases:

```text
phase15_biological_literature_support/
phase16_manuscript_figures_package/
phase17_repeated_cross_validation_robust_benchmark/
phase22_multimodal_fusion_strategy_comparison/
phase23_leakage_and_bias_audit/
phase23b_bias_controlled_robustness_audit/
phase24_topk_ranking_utility_metrics/
phase25_final_manuscript_results_integration/
```

## Reproducibility

The project was developed in Python using common scientific machine learning libraries.

To create the environment using `pip`:

```bash
pip install -r requirements.txt
```

Or using Conda:

```bash
conda env create -f environment.yml
conda activate t2d_gene_prioritization
```

The executable workflow is provided through the phase folders. Each phase folder contains the relevant code/notebook and outputs for that stage.

## Data availability and licensing

This repository may include processed datasets, split IDs, metadata, final output tables, and derived features where redistribution is allowed.

Raw third-party data files are not necessarily redistributed. If a raw database or genome/proteome file is subject to external licensing restrictions, it should be excluded from the public repository and documented in `DATA_LICENSE_NOTICE.md`.

## Manuscript

The final manuscript files are stored in:

```text
manuscript/
```

The final figures are stored in:

```text
figures/
```

The graphical abstract is stored in:

```text
graphical_abstract/
```

## Citation

If you use this repository, please cite the associated manuscript and this repository. Citation metadata is provided in `CITATION.cff`.

## Repository

GitHub: https://github.com/akaaan25112002/Project_Protein_GitHub_Public

## Contact

Khoa Nguyen Anh
Email: khoa.nguyenanh2511@gmail.com
