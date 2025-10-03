# Assignment 3: EEG Processing

The project focused on analyzing EEG data from a visual categorization task (faces vs. dollhouses). The main steps I implemented are:

1. **Preprocessing**

   * Applied filtering, epoching, and baseline correction to raw EEG.
   * Used artifact rejection methods (including ICA) to clean the data.

2. **Event-Related Potentials (ERP)**

   * Computed ERPs for face vs. dollhouse trials.
   * Conducted statistical comparisons to identify significant category-related differences.

3. **Time-Frequency Analysis**

   * Performed wavelet-based spectral analysis.
   * Compared oscillatory activity (alpha, beta, gamma) across stimulus categories.

4. **Multivariate Pattern Analysis (MVPA)**

   * Applied temporal and spatial MVPA to decode face vs. dollhouse stimuli.
   * Explored cross-temporal generalization to study dynamics of representation.

5. **Representational Dissimilarity & RSA**

   * Built Representational Dissimilarity Matrices (RDMs) from EEG activity.
   * Compared EEG RDMs to visual-layer features from the **CORnet-S** deep neural network.
   * Interpreted correlations in terms of ventral visual stream dynamics.

### Summary

This assignment combined **signal preprocessing, ERP analysis, spectral methods, machine learning, and representational similarity analysis** to investigate how the brain distinguishes visual categories using EEG.
