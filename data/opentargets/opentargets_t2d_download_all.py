import json
import math
import time
from pathlib import Path

import pandas as pd
import requests


# ============================================================
# CONFIG
# ============================================================

GRAPHQL_URL = "https://api.platform.opentargets.org/api/v4/graphql"

DISEASE_ID = "MONDO_0005148"
PAGE_SIZE = 500
ENABLE_INDIRECT = False   # Direct only; direct/indirect gave same count in your check
SLEEP_SECONDS = 0.2       # Polite delay between API calls

OUTPUT_DIR = Path("opentargets_t2d_output")
OUTPUT_DIR.mkdir(exist_ok=True)

RAW_JSON_PATH = OUTPUT_DIR / "opentargets_t2d_all_pages_raw.json"
CSV_PATH = OUTPUT_DIR / "opentargets_t2d_associated_targets_all.csv"


# ============================================================
# GRAPHQL QUERY
# ============================================================

QUERY = """
query DiseaseAssociationsQuery(
  $id: String!
  $index: Int!
  $size: Int!
  $sortBy: String!
  $enableIndirect: Boolean!
  $datasources: [DatasourceSettingsInput!]
  $rowsFilter: [String!]
  $facetFilters: [String!]
  $entitySearch: String!
) {
  disease(efoId: $id) {
    id
    name
    associatedTargets(
      page: { index: $index, size: $size }
      orderByScore: $sortBy
      enableIndirect: $enableIndirect
      datasources: $datasources
      Bs: $rowsFilter
      facetFilters: $facetFilters
      BFilter: $entitySearch
    ) {
      count
      rows {
        target {
          id
          approvedSymbol
          approvedName
          prioritisation {
            items {
              key
              value
            }
          }
        }
        score
        datasourceScores {
          componentId: id
          score
        }
      }
    }
  }
}
"""


# Same datasource configuration exported by the Open Targets web UI
DATASOURCES = [
    {"id": "clinical_precedence", "weight": 1, "propagate": True, "required": False},
    {"id": "gwas_credible_sets", "weight": 1, "propagate": True, "required": False},
    {"id": "gene_burden", "weight": 1, "propagate": True, "required": False},
    {"id": "eva", "weight": 1, "propagate": True, "required": False},
    {"id": "genomics_england", "weight": 1, "propagate": True, "required": False},
    {"id": "gene2phenotype", "weight": 1, "propagate": True, "required": False},
    {"id": "uniprot_literature", "weight": 1, "propagate": True, "required": False},
    {"id": "uniprot_variants", "weight": 1, "propagate": True, "required": False},
    {"id": "orphanet", "weight": 1, "propagate": True, "required": False},
    {"id": "clingen", "weight": 1, "propagate": True, "required": False},
    {"id": "cancer_gene_census", "weight": 1, "propagate": True, "required": False},
    {"id": "intogen", "weight": 1, "propagate": True, "required": False},
    {"id": "eva_somatic", "weight": 1, "propagate": True, "required": False},
    {"id": "cancer_biomarkers", "weight": 1, "propagate": True, "required": False},
    {"id": "crispr_screen", "weight": 1, "propagate": True, "required": False},
    {"id": "crispr", "weight": 1, "propagate": True, "required": False},
    {"id": "reactome", "weight": 1, "propagate": True, "required": False},
    {"id": "europepmc", "weight": 0.2, "propagate": True, "required": False},
    {"id": "expression_atlas", "weight": 0.2, "propagate": False, "required": False},
    {"id": "impc", "weight": 0.2, "propagate": True, "required": False},
    {"id": "ot_crispr_validation", "weight": 0.5, "propagate": True, "required": False},
    {"id": "ot_crispr", "weight": 0.5, "propagate": True, "required": False},
    {"id": "encore", "weight": 0.5, "propagate": True, "required": False},
]


# ============================================================
# API HELPERS
# ============================================================

def build_variables(page_index: int, page_size: int) -> dict:
    return {
        "id": DISEASE_ID,
        "index": page_index,
        "size": page_size,
        "sortBy": "score",
        "enableIndirect": ENABLE_INDIRECT,
        "datasources": DATASOURCES,
        "rowsFilter": [],
        "facetFilters": [],
        "entitySearch": "",
    }


def fetch_page(page_index: int, page_size: int) -> dict:
    payload = {
        "query": QUERY,
        "variables": build_variables(page_index, page_size),
    }

    response = requests.post(
        GRAPHQL_URL,
        json=payload,
        timeout=120,
    )
    response.raise_for_status()

    data = response.json()

    if "errors" in data:
        raise RuntimeError(
            f"GraphQL returned errors on page {page_index}:\n"
            f"{json.dumps(data['errors'], indent=2)}"
        )

    disease = data.get("data", {}).get("disease")
    if disease is None:
        raise RuntimeError(f"No disease block returned on page {page_index}.")

    assoc = disease.get("associatedTargets")
    if assoc is None:
        raise RuntimeError(f"No associatedTargets block returned on page {page_index}.")

    return data


def flatten_row(row: dict, rank: int) -> dict:
    target = row.get("target", {}) or {}

    record = {
        "rank_by_score": rank,
        "disease_id": DISEASE_ID,
        "evidence_mode": "direct_only" if not ENABLE_INDIRECT else "direct_plus_indirect",
        "target_id": target.get("id"),
        "target_symbol": target.get("approvedSymbol"),
        "target_name": target.get("approvedName"),
        "association_score": row.get("score"),
    }

    # Flatten datasource scores
    for ds in row.get("datasourceScores", []) or []:
        component_id = ds.get("componentId")
        if component_id:
            record[f"ds_{component_id}"] = ds.get("score")

    # Flatten prioritisation items
    prioritisation = target.get("prioritisation") or {}
    for item in prioritisation.get("items", []) or []:
        key = item.get("key")
        if key:
            record[f"prio_{key}"] = item.get("value")

    return record


# ============================================================
# MAIN DOWNLOAD PIPELINE
# ============================================================

def main():
    print("=" * 110)
    print("Open Targets — Type 2 Diabetes Mellitus Associated Targets")
    print(f"Disease ID: {DISEASE_ID}")
    print(f"GraphQL endpoint: {GRAPHQL_URL}")
    print(f"Page size: {PAGE_SIZE}")
    print(f"Enable indirect: {ENABLE_INDIRECT}")
    print("=" * 110)

    # --------------------------------------------------------
    # 1. Fetch first page to learn total count
    # --------------------------------------------------------
    first_page = fetch_page(page_index=0, page_size=PAGE_SIZE)

    disease_block = first_page["data"]["disease"]
    assoc_block = disease_block["associatedTargets"]

    disease_name = disease_block["name"]
    total_count = assoc_block["count"]
    total_pages = math.ceil(total_count / PAGE_SIZE)

    print(f"\nDisease name: {disease_name}")
    print(f"Total associations reported by API: {total_count}")
    print(f"Total pages to download: {total_pages}")

    all_raw_pages = [first_page]
    all_rows = list(assoc_block["rows"])

    print(
        f"Downloaded page 1/{total_pages} | "
        f"rows this page: {len(assoc_block['rows'])} | "
        f"cumulative rows: {len(all_rows)}"
    )

    # --------------------------------------------------------
    # 2. Fetch remaining pages
    # --------------------------------------------------------
    for page_index in range(1, total_pages):
        time.sleep(SLEEP_SECONDS)

        page_data = fetch_page(page_index=page_index, page_size=PAGE_SIZE)
        page_assoc = page_data["data"]["disease"]["associatedTargets"]
        page_rows = page_assoc["rows"]

        all_raw_pages.append(page_data)
        all_rows.extend(page_rows)

        print(
            f"Downloaded page {page_index + 1}/{total_pages} | "
            f"rows this page: {len(page_rows)} | "
            f"cumulative rows: {len(all_rows)}"
        )

    # --------------------------------------------------------
    # 3. Validation checks
    # --------------------------------------------------------
    print("\n" + "-" * 110)
    print("Validation")

    print(f"Expected row count from API: {total_count}")
    print(f"Downloaded row count:         {len(all_rows)}")

    if len(all_rows) != total_count:
        print(
            "WARNING: Downloaded rows do not match reported total count. "
            "Inspect before using as a final dataset."
        )
    else:
        print("Row count check passed.")

    # --------------------------------------------------------
    # 4. Save raw JSON pages
    # --------------------------------------------------------
    with RAW_JSON_PATH.open("w", encoding="utf-8") as f:
        json.dump(all_raw_pages, f, indent=2, ensure_ascii=False)

    print(f"\nSaved raw JSON pages to:\n{RAW_JSON_PATH}")

    # --------------------------------------------------------
    # 5. Flatten to DataFrame
    # --------------------------------------------------------
    records = [
        flatten_row(row, rank=i + 1)
        for i, row in enumerate(all_rows)
    ]

    df = pd.DataFrame(records)

    # Make sure score is numeric
    if "association_score" in df.columns:
        df["association_score"] = pd.to_numeric(
            df["association_score"],
            errors="coerce"
        )

    # Sort consistently
    df = df.sort_values(
        by=["association_score", "target_symbol"],
        ascending=[False, True],
        na_position="last"
    ).reset_index(drop=True)

    # Rebuild rank after sorting
    df["rank_by_score"] = range(1, len(df) + 1)

    # --------------------------------------------------------
    # 6. Save CSV
    # --------------------------------------------------------
    df.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")
    print(f"Saved flattened CSV to:\n{CSV_PATH}")

    # --------------------------------------------------------
    # 7. Quick summary
    # --------------------------------------------------------
    print("\n" + "=" * 110)
    print("Quick summary")
    print("=" * 110)

    print(f"DataFrame shape: {df.shape}")
    print(f"Unique target IDs: {df['target_id'].nunique(dropna=True)}")
    print(f"Unique target symbols: {df['target_symbol'].nunique(dropna=True)}")

    print("\nAssociation score summary:")
    print(df["association_score"].describe().to_string())

    print("\nTop 20 targets:")
    print(
        df[
            ["rank_by_score", "target_symbol", "target_name", "association_score"]
        ]
        .head(20)
        .to_string(index=False)
    )

    ds_cols = [c for c in df.columns if c.startswith("ds_")]
    if ds_cols:
        datasource_coverage = pd.DataFrame({
            "datasource": ds_cols,
            "non_null_count": [df[c].notna().sum() for c in ds_cols],
            "coverage_pct": [df[c].notna().mean() * 100 for c in ds_cols],
            "mean_score_when_present": [df[c].dropna().mean() for c in ds_cols],
        }).sort_values(
            by=["non_null_count", "mean_score_when_present"],
            ascending=[False, False]
        )

        print("\nDatasource coverage:")
        print(datasource_coverage.to_string(index=False))

        datasource_coverage.to_csv(
            OUTPUT_DIR / "opentargets_t2d_datasource_coverage.csv",
            index=False,
            encoding="utf-8-sig"
        )

    print("\nDone.")


if __name__ == "__main__":
    main()