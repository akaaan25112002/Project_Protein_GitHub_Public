# Leakage-Safe Explainable Multi-Omics Framework for Type 2 Diabetes Gene Prioritization

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21489228.svg)](https://doi.org/10.5281/zenodo.21489228)

## Overview

This repository accompanies the manuscript:

> **Leakage-Safe Explainable Multi-Omics Framework for Type 2 Diabetes Gene Prioritization Using Protein and Genomic Sequence Representations**

The project presents a **gene/protein prioritization framework** that integrates protein sequence embeddings, genomic regulatory sequence representations, multimodal machine learning, explainability analysis, and biological validation under a leakage-aware evaluation protocol.

Unlike patient-level diagnostic models, this work focuses on **prioritizing T2D-associated genes and proteins** for downstream biological interpretation and hypothesis generation.

---

## Highlights

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

## Research Scope

This repository **does NOT** implement a clinical diagnosis system.

The prediction target is:
> **candidate T2D gene/protein prioritization**

Model outputs should **not** be interpreted as:
- Patient diagnosis / Disease probability
- Clinical risk prediction / Causal evidence

Instead, the framework is intended to assist computational prioritization of candidate genes for downstream biological investigation.

---

## Repository Structure

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
├── manuscript/          # Manuscript source files
├── data/                # Data directories (GWAS, UniProt, OpenTargets, processed)
├── notebooks/           # Phase-based Jupyter notebooks
├── model/               # Trained model checkpoints
├── figures/             # Generated publication figures
├── graphical_abstract/  # Graphical abstract assets
├── supplementary/       # Supplementary materials
└── results/             # Evaluation tables and statistical outputs
```

---

## Workflow & Phase Organization

The repository follows a sequential, phase-based research pipeline. Execute the notebooks in `notebooks/` chronologically to reproduce the complete study.

```text
Dataset Construction ➔ Sequence Feature Extraction ➔ Embedding Generation ➔ Multimodal Integration ➔ Robust Evaluation ➔ Explainability & Validation
```

| Phase | Purpose | Phase | Purpose |
| :--- | :--- | :--- | :--- |
| **Phase 1** | Dataset construction | **Phase 14** | Explainability analysis |
| **Phase 2** | Protein embedding | **Phase 15** | Biological validation |
| **Phase 3** | Baseline models | **Phase 16** | Manuscript figures generation |
| **Phase 10** | Modality contribution | **Phase 17** | Robust repeated benchmarking |
| **Phase 11** | Repeated robustness | **Phase 18** | Negative-set sensitivity |
| **Phase 12** | Random gene-set analysis | **Phase 19** | External validation |
| **Phase 13** | Statistical calibration | **Phase 20–21** | Genomic preprocessing |
| **Phase 22** | Fusion strategy comparison | **Phase 23** | Leakage and bias audit |
| **Phase 23B**| Bias-controlled robustness | **Phase 24** | Top-K ranking utility |

---

## Installation & Setup

### Option 1: Using Pip (Recommended with venv)
```bash
# Create and activate environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Using Conda
```bash
conda env create -f environment.yml
conda activate t2d_gene_prioritization
```

---

## Reproducibility & Data Availability

All frozen datasets, processed feature matrices, trained model checkpoints, evaluation tables, and generated manuscript/supplementary figures supporting this study are permanently archived on Zenodo.

- **Zenodo Archive & DOI:** [https://doi.org/10.5281/zenodo.21489228](https://doi.org/10.5281/zenodo.21489228)
- **Data Sources:** Integrates data from GWAS Catalog, Open Targets Platform, UniProt, and regulatory genomic sequence resources. (See `DATA_LICENSE_NOTICE.md` for license details).

---

## Citation

If this repository or the associated framework contributes to your research, please cite using the metadata provided in `CITATION.cff`.

---

## Contact

*   **Nguyen Anh Khoa** (Repository Maintainer)  
    Faculty of Information Technology, Swinburne Vietnam  
    Email: [khoa.nguyenanh2511@gmail.com](mailto:khoa.nguyenanh2511@gmail.com)
*   **Sandhya Dubey** (Corresponding Author)  
    Manipal Academy of Higher Education  
    Email: [sandhya.dubey@manipal.edu](mailto:sandhya.dubey@manipal.edu)
