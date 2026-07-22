# Leakage-Safe Explainable Multi-Omics Framework for Type 2 Diabetes Gene Prioritization

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![DOI](https://img.shields.io/badge/DOI-Coming%20Soon-lightgrey.svg)]()

## Overview

This repository accompanies the manuscript:

> **Leakage-Safe Explainable Multi-Omics Framework for Type 2 Diabetes Gene Prioritization Using Protein and Genomic Sequence Representations**

The project presents a **gene/protein prioritization framework** that integrates protein sequence embeddings, genomic regulatory sequence representations, multimodal machine learning, explainability analysis, and biological validation under a leakage-aware evaluation protocol.

Unlike patient-level diagnostic models, this work focuses on **prioritizing T2D-associated genes and proteins** for downstream biological interpretation and hypothesis generation.

---

# Highlights

The framework includes:

- Leakage-safe multimodal machine learning pipeline
- Protein and genomic sequence representations
- Repeated-split robustness evaluation
- Paired statistical testing with BH-FDR correction
- Explainability using block-level feature analysis
- Literature-supported biological validation
- Top-K ranking utility evaluation
- Bias and negative-set sensitivity auditing
- Fully reproducible phase-based research workflow

---

# Research Scope

This repository **does NOT** implement a clinical diagnosis system.

The prediction target is

> **candidate T2D gene/protein prioritization**

Model outputs should **not** be interpreted as:

- patient diagnosis
- disease probability
- clinical risk prediction
- causal evidence

Instead, the framework is intended to assist computational prioritization of candidate genes for downstream biological investigation.

---

# Repository Structure

```text
Project_Protein_GitHub_Public/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── DATA_LICENSE_NOTICE.md
├── requirements.txt
├── environment.yml
│
├── manuscript/
│
├── data/
│   ├── GWAS/
│   ├── UniProt/
│   ├── OpenTargets/
│   └── processed/
│
├── notebooks/
│
├── model/
│
├── figures/
│
├── graphical_abstract/
│
├── supplementary/
│
└── results/
```

---

# Workflow

The repository follows the complete research workflow used in the manuscript.

```text
Phase 1
Dataset construction
        │
        ▼
Protein sequence extraction
        │
        ▼
Genomic regulatory sequence extraction
        │
        ▼
Feature engineering
        │
        ▼
Protein embedding generation
        │
        ▼
Baseline model development
        │
        ▼
Multimodal integration
        │
        ▼
Robust repeated evaluation
        │
        ▼
Explainability analysis
        │
        ▼
Biological validation
        │
        ▼
Bias auditing
        │
        ▼
Top-K prioritization
        │
        ▼
Final manuscript generation
```

---

# Phase Organization

Each notebook corresponds to one stage of the research pipeline.

Examples include:

| Phase | Purpose |
|-------|---------|
| Phase 1 | Dataset construction |
| Phase 2 | Protein embedding |
| Phase 3 | Baseline models |
| Phase 10 | Modality contribution |
| Phase 11 | Repeated robustness |
| Phase 12 | Random gene-set analysis |
| Phase 13 | Statistical calibration |
| Phase 14 | Explainability |
| Phase 15 | Biological validation |
| Phase 16 | Manuscript figures |
| Phase 17 | Robust repeated benchmarking |
| Phase 18 | Negative-set sensitivity |
| Phase 19 | External validation |
| Phase 20–21 | Genomic preprocessing |
| Phase 22 | Fusion strategy comparison |
| Phase 23 | Leakage and bias audit |
| Phase 23B | Bias-controlled robustness |
| Phase 24 | Top-K ranking utility |

---

# Main Contributions

The manuscript is primarily supported by the following analyses:

- Leakage-safe evaluation strategy
- Protein versus genomic representation comparison
- Handcrafted versus foundation-model features
- Multimodal integration strategies
- Explainability analysis
- Biological pathway validation
- Literature-supported candidate prioritization
- Top-K recovery analysis
- Negative-set robustness auditing

---

# Installation

Using pip

```bash
pip install -r requirements.txt
```

Using Conda

```bash
conda env create -f environment.yml
conda activate t2d_gene_prioritization
```

---

# Reproducing the Study

The workflow can be reproduced by executing the phase notebooks sequentially.

Each notebook contains:

- preprocessing
- model training
- evaluation
- visualization
- exported manuscript figures

---

# Data Sources

The project integrates information from publicly available biological resources including:

- GWAS Catalog
- Open Targets Platform
- UniProt
- Protein sequence databases
- Regulatory genomic sequence resources

Please refer to `DATA_LICENSE_NOTICE.md` for redistribution restrictions of third-party datasets.

---

# Outputs

Repository outputs include:

- trained models
- processed datasets
- manuscript figures
- supplementary figures
- evaluation tables
- statistical analyses
- explainability results

---

# Manuscript

The manuscript source is available in

```text
manuscript/
```

Generated publication figures are located in

```text
figures/
```

The graphical abstract is located in

```text
graphical_abstract/
```

---

# Reproducibility

The project was developed under a reproducible research workflow.

Random seeds, evaluation protocols, repeated validation, and statistical analyses are documented throughout the notebooks.

---

# Data Availability

Processed datasets, trained models, evaluation outputs, and manuscript figures are publicly available through this repository.

Zenodo archival DOI will be added upon publication.

---

# Citation

If this repository contributes to your research, please cite both:

- the associated manuscript
- this GitHub repository

Citation metadata is provided in `CITATION.cff`.

---

# Repository

GitHub

https://github.com/akaaan25112002/Project_Protein_GitHub_Public

Zenodo DOI

**Coming Soon**

---

# Contact

**Nguyen Anh Khoa**

Faculty of Information Technology  
Swinburne Vietnam  
Swinburne University of Technology

Email:
khoa.nguyenanh2511@gmail.com