## Methods - Corrected Genomic Feature Mapping

For handcrafted genomic explainability, feature names were mapped to interpretable sequence feature groups. The K3/K4/Basic representation contained 356 features, corresponding to K3 k-mer, K4 k-mer and basic sequence-composition features. Feature groups included K3 k-mers, K4 k-mers, GC-content features, CpG-related features, skew features, nucleotide-composition features and other basic descriptors. Original feature names were loaded from the saved feature-name file. Feature-level permutation importance and SHAP values were then aggregated at the feature-group level to provide interpretable summaries of genomic model behaviour.

## Results - Corrected Genomic Explainability

After correcting the genomic feature mapping, grouped permutation importance and SHAP summaries were recalculated for the handcrafted genomic explainability model. This allowed the genomic contribution to be interpreted by feature type rather than by anonymous feature index. The grouped analysis identified which categories of sequence features contributed most strongly to the genomic random forest explainability model. These results provide feature-group-level support for the explainable component of the framework, while still requiring cautious interpretation because the final predictive models use high-dimensional protein and genomic representations.

## Discussion - Corrected Explainability Interpretation

The corrected feature mapping improves the interpretability of the handcrafted genomic representation. Unlike DNABERT-2 embeddings, which are latent and difficult to interpret directly, handcrafted genomic features can be grouped into explicit biological sequence descriptors such as k-mer composition, GC/CpG content and skew features. This supports the interpretation that handcrafted genomic features are less powerful as standalone predictors but more transparent. Therefore, the explainability analysis strengthens the central ranking-versus-interpretability narrative: DNABERT-2 embeddings may contribute more strongly to ranking behaviour, while handcrafted genomic features provide more direct feature-level interpretability.

