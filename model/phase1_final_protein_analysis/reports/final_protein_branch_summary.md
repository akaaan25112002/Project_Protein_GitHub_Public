
# Final Protein Branch Summary

The protein representation branch compared handcrafted protein descriptors, ESM-2 embeddings, and ProtBERT embeddings for T2D-associated protein classification.

The handcrafted AAC + physicochemical baseline achieved weak test performance:
- ROC-AUC = 0.5520
- PR-AUC = 0.5550
- F1 = 0.5390
- MCC = 0.0480

Protein foundation embeddings improved performance substantially.

Best final-selected representation by ROC-AUC:
- Phase: 1.2E
- Representation: ProtBERT
- Embedding policy: sliding_window_1022_stride_1022
- Final model: Logistic Regression
- Test ROC-AUC = 0.6487
- Test PR-AUC = 0.6551
- Test F1 = 0.5896
- Test MCC = 0.1941

Best final-selected representation by F1:
- Phase: 1.2D
- Representation: ProtBERT
- Embedding policy: truncated_1022
- Final model: Logistic Regression
- Test F1 = 0.6014

Best final-selected representation by MCC:
- Phase: 1.2D
- Representation: ProtBERT
- Embedding policy: truncated_1022
- Final model: Logistic Regression
- Test MCC = 0.1943

Main conclusion:
Protein language model embeddings outperform handcrafted descriptors.
ProtBERT is the strongest representation family in this protein-only branch.
However, performance remains moderate, suggesting that protein sequence alone is insufficient for highly accurate T2D association prediction.
The next stage should integrate genomic, regulatory, pathway, or evidence-based features.
