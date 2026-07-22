# Leakage-Safe Explainable Multi-Omics Framework for Type 2 Diabetes Gene Prioritization Using Protein and Genomic Sequence Representations

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21489228.svg)](https://doi.org/10.5281/zenodo.21489228)

---

## Overview

This repository accompanies the research manuscript:

> **Leakage-Safe Explainable Multi-Omics Framework for Type 2 Diabetes Gene Prioritization Using Protein and Genomic Sequence Representations**

The framework introduces a **leakage-safe, explainable, multimodal computational pipeline** for prioritizing Type 2 Diabetes (T2D)-associated genes using complementary protein and genomic sequence representations.

Rather than performing patient-level diagnosis, the framework aims to prioritize candidate genes for downstream biological interpretation and hypothesis generation.

---

## Highlights

The repository provides a complete and reproducible implementation of the proposed framework, including:

- Leakage-safe evaluation protocol
- Protein language model embeddings (ProtBERT)
- Genomic regulatory sequence representations
- Handcrafted genomic features
- DNABERT-2 genomic embeddings
- Multimodal feature integration
- Repeated-split robustness evaluation
- Paired statistical testing with BH-FDR correction
- Explainability analysis
- Biological validation
- Top-K gene prioritization analysis
- Negative-set sensitivity analysis
- Leakage and bias auditing
- Publication-ready figures and supplementary analyses

---

## Research Scope

This repository **does not implement a clinical diagnosis model.**

The prediction target is

> **Candidate Type 2 Diabetes gene/protein prioritization.**

The model outputs should **NOT** be interpreted as

- patient diagnosis
- disease probability
- clinical risk prediction
- causal inference

Instead, the framework is designed to prioritize biologically relevant candidate genes for downstream experimental investigation.

---

## Repository Structure

```text
Project_Protein_GitHub_Public/

README.md
LICENSE
CITATION.cff
DATA_LICENSE_NOTICE.md

requirements.txt
environment.yml

data/
    GWAS/
    UniProt/
    opentargets/

model/

notebooks/

graphical_abstract/

manuscript/

figures/

results/
```

---

## Phase-Based Workflow

The project follows a complete end-to-end research pipeline.

```text
Dataset Construction
        ↓
Protein Sequence Processing
        ↓
Genomic Sequence Processing
        ↓
Feature Engineering
        ↓
Protein Embedding Extraction
        ↓
Multimodal Integration
        ↓
Model Training
        ↓
Repeated Evaluation
        ↓
Statistical Validation
        ↓
Explainability
        ↓
Biological Validation
        ↓
Bias & Leakage Audit
        ↓
Final Manuscript
```

Major analysis stages include:

| Phase | Description |
|---------|------------|
| Phase 1 | Dataset construction |
| Phase 2 | Protein feature extraction |
| Phase 3 | Protein baseline models |
| Phase 10 | Modality contribution |
| Phase 11 | Repeated robustness evaluation |
| Phase 12 | Random gene-set validation |
| Phase 13 | Statistical calibration |
| Phase 14 | Explainability analysis |
| Phase 15 | Literature-supported biological validation |
| Phase 16 | Manuscript figure generation |
| Phase 17 | Robust repeated benchmarking |
| Phase 18 | Negative-set sensitivity analysis |
| Phase 19 | External validation |
| Phase 20 | Genomic dataset preprocessing |
| Phase 21 | Handcrafted genomic feature engineering |
| Phase 22 | Fusion strategy comparison |
| Phase 23 | Leakage and bias auditing |
| Phase 23B | Bias-controlled robustness audit |
| Phase 24 | Top-K ranking utility analysis |

---

## Installation

### Using pip

```bash
python -m venv venv

source venv/bin/activate
# Windows:
# venv\Scripts\activate

pip install -r requirements.txt
```

### Using Conda

```bash
conda env create -f environment.yml

conda activate t2d_gene_prioritization
```

---

## Reproducing the Study

Execute the notebooks sequentially inside the `notebooks/` directory.

The output generated from each phase is used as the input for subsequent analyses.

The final manuscript results are reproduced through the complete phase-based workflow.

---

## Data Availability

All processed datasets, trained models, evaluation tables, manuscript figures and supplementary outputs supporting this study are permanently archived on Zenodo.

**Zenodo DOI**

https://doi.org/10.5281/zenodo.21489228

Raw third-party resources (e.g., UniProt, Open Targets, GWAS Catalog and Ensembl-derived data) remain subject to their original licenses and are documented in `DATA_LICENSE_NOTICE.md`.

---

## Citation

If this repository contributes to your research, please cite both:

- the associated manuscript
- this GitHub repository

Citation metadata is provided in `CITATION.cff`.

---

## License

Released under the MIT License.

---

## Acknowledgements

This work was conducted at

- Department of Computer Science and Engineering,
  Manipal Institute of Technology,
  Manipal Academy of Higher Education,
  India

in collaboration with

- Swinburne Vietnam,
  Swinburne University of Technology.

---

## Contact

### Anh Khoa Nguyen

Swinburne Vietnam

Email:

khoa.nguyenanh2511@gmail.com

---

GitHub

https://github.com/akaaan25112002/Project_Protein_GitHub_Public

Zenodo

https://doi.org/10.5281/zenodo.21489228