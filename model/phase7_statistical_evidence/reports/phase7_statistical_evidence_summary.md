# Phase 7 — Statistical Evidence Strengthening Report

## Objective

This phase estimated uncertainty around model performance using nonparametric bootstrap confidence intervals and paired bootstrap comparisons. The goal was to evaluate whether observed differences between protein-only, genomic-only, handcrafted multimodal, and DNABERT-2 multimodal models are meaningful on the same held-out test set.

## Best Models by Ranking Metrics

- Best ROC-AUC model: **Multimodal_DNABERT2**, ROC-AUC = 0.7568 [0.7002, 0.8108].

- Best PR-AUC model: **Multimodal_handcrafted**, PR-AUC = 0.7573 [0.6893, 0.8212].

## Focused Comparison: DNABERT-2 Multimodal vs Handcrafted Multimodal

- roc_auc: delta = 0.0278, 95% CI [0.0015, 0.0540], bootstrap p = 0.0396, interpretation = significant.

- pr_auc: delta = -0.0126, 95% CI [-0.0552, 0.0298], bootstrap p = 0.5980, interpretation = not_significant_or_uncertain.


## Interpretation Guide

If a pairwise delta confidence interval includes zero, the difference should be interpreted as uncertain or not statistically robust under bootstrap resampling. If the interval excludes zero, the improvement is more strongly supported. ROC-AUC and PR-AUC are threshold-independent, while F1 and MCC depend on the selected classification threshold.
