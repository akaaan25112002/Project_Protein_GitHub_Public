# Phase 13 — Statistical and Claim Calibration

## Objective

This phase addresses the latest feedback by replacing unpaired-style interpretation of the repeated-split evaluation with paired statistical tests, and by calibrating the biological interpretation to match the FDR-corrected evidence.

## Paired Seed Comparison

Because the repeated-split evaluation used the same random seeds for each model, model differences were analysed as paired deltas:

delta_i = metric_DNABERT2(seed_i) − metric_handcrafted(seed_i)

The primary paired test was the Wilcoxon signed-rank test. Paired t-tests and exact sign tests were included as supportive checks. BH-FDR correction was applied across the four Wilcoxon tests.

| Metric                                    |   Mean Δ D2−HC | 95% CI of Δ       | Bootstrap 95% CI   |   Wilcoxon p |   Wilcoxon BH-FDR p |   Paired t-test p |   Sign-test p |   Wins D2/10 |   Wins HC/10 | Δ range           |   Cohen dz |   Rank-biserial r | Interpretation                                                                                                                                              |
|:------------------------------------------|---------------:|:------------------|:-------------------|-------------:|--------------------:|------------------:|--------------:|-------------:|-------------:|:------------------|-----------:|------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PR-AUC (Primary ranking metric)           |         0.0009 | [-0.0053, 0.0070] | [-0.0042, 0.0059]  |       0.9434 |              0.9434 |            0.7595 |        1      |            5 |            5 | -0.0126 to 0.0141 |     0.0998 |            0.0364 | PR-AUC is essentially tied between DNABERT-2 and handcrafted multimodal. This supports comparable primary ranking performance, not DNABERT-2 superiority.   |
| MCC (Primary threshold-dependent metric)  |         0.0271 | [-0.0167, 0.0709] | [-0.0088, 0.0633]  |       0.1934 |              0.2578 |            0.1954 |        0.3438 |            7 |            3 | -0.0689 to 0.1175 |     0.4423 |            0.4909 | DNABERT-2 is numerically higher, but the paired difference is not statistically significant after BH correction. Interpret as directional, not established. |
| ROC-AUC (Secondary global ranking metric) |         0.0103 | [0.0017, 0.0190]  | [0.0030, 0.0173]   |       0.0273 |              0.1094 |            0.0242 |        0.1094 |            8 |            2 | -0.0133 to 0.0283 |     0.8552 |            0.7818 | DNABERT-2 is numerically higher, but the paired difference is not statistically significant after BH correction. Interpret as directional, not established. |
| F1 (Secondary threshold-dependent metric) |         0.0236 | [-0.0332, 0.0805] | [-0.0216, 0.0682]  |       0.084  |              0.168  |            0.3718 |        0.1094 |            8 |            2 | -0.1392 to 0.1445 |     0.2972 |            0.6364 | DNABERT-2 is numerically higher, but the paired difference is not statistically significant after BH correction. Interpret as directional, not established. |

## Calibrated Statistical Interpretation

Across 10 paired splits, DNABERT-2 showed numerically higher ROC-AUC, MCC and F1 and essentially tied PR-AUC. However, the paired tests did not establish statistically significant superiority after BH correction. Therefore, DNABERT-2 should be described as showing a small, directionally repeatable but not statistically established global-ranking advantage.

## Moved-in / Moved-out Comparator

Moved-in and moved-out genes were defined relative to the handcrafted multimodal ranking. Moved-in genes are inside DNABERT-2 top-N but outside handcrafted top-N. Moved-out genes are inside handcrafted top-N but outside DNABERT-2 top-N.

## Moved-in Top-50 Baseline

DNABERT-2 moved-in top-50 genes contained zero genes across the curated T2D, beta-cell, glucose, mitochondrial/OXPHOS, insulin-signalling, pancreatic-development and lipid-metabolism themes. Same-size random baselines show that these low-frequency themes often have low or zero counts in random sets. Therefore, this should be interpreted as absence of curated-theme enrichment, not as statistically significant depletion.

## Moved-out Top-50 Baseline

The moved-out top-50 genes contained 3 mitochondrial-function genes (NDUFA7;NDUFB1;NDUFB3) compared with random mean 0.430 ± 0.648 (empirical p=0.0100, FDR p=0.1598). They also contained 3 OXPHOS genes (NDUFA7;NDUFB1;NDUFB3) compared with random mean 0.410 ± 0.618 (empirical p=0.0070, FDR p=0.1598). These results are nominally enriched but not FDR-significant, so they should be treated as hypothesis-generating.

## Revised Central Interpretation

The calibrated interpretation is that the results are consistent with a ranking-versus-interpretability trade-off. DNABERT-2 shows small, directionally repeatable numerical gains in several metrics but not statistically established superiority after paired testing and BH correction. Meanwhile, handcrafted/protein rankings show suggestive mitochondrial/OXPHOS concentration among top candidates, but the biological evidence is FDR-borderline and based on small gene counts. Therefore, the trade-off should be presented as a central hypothesis-generating finding rather than a definitive effect.