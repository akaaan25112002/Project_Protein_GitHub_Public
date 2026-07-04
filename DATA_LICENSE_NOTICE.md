# Data License Notice

This repository is intended to provide reproducible supporting materials for a gene/protein-level Type 2 Diabetes candidate prioritization study.

## Public data policy

The repository may include:

- processed gene/protein-level datasets;
- derived feature matrices where redistribution is allowed;
- split identifiers;
- metadata tables;
- final prediction outputs;
- evaluation tables;
- figures;
- manuscript-supporting results.

## Raw third-party data

Raw third-party data should not be redistributed unless the original license explicitly permits redistribution.

This includes, but is not limited to:

- raw genome FASTA files;
- raw proteome FASTA files;
- raw database dumps;
- raw GWAS catalog exports;
- raw Open Targets exports;
- raw DisGeNET or disease-gene database exports;
- other external resources with redistribution restrictions.

If raw files are required to reproduce the analysis, the repository should instead provide:

1. the source name;
2. accession or query information;
3. download date;
4. preprocessing description;
5. processed output files where redistribution is allowed;
6. split IDs and metadata needed for reproducibility.

## Recommended location for non-public data

Restricted or large raw files should be kept outside the public repository or placed under:

```text
data/raw/
restricted_data/
```

These locations are excluded by `.gitignore`.

## Interpretation note

The dataset supports gene/protein-level candidate prioritization. It should not be interpreted as patient-level clinical data.
