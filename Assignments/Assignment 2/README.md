# Assigment 2 - Spike Sorting and Neural Data Analysis

The project focused on analyzing extracellular neural recordings and implementing spike sorting and neural data analysis.

### What I Did

1. **Spike Sorting from Scratch**

   * Loaded raw extracellular voltage signals and visualized them.
   * Applied a **Butterworth high-pass filter (300 Hz)** to remove low-frequency noise.
   * Detected spikes using a threshold based on noise estimation (θ = 5σn).
   * Extracted spike waveforms (2 ms before and after each peak).
   * Applied **PCA** for feature extraction and used **K-means clustering** to group spikes.
   * Evaluated clustering with the elbow method and also tried **t-SNE features** for comparison.

2. **Spike Sorting with ROSS**

   * Used the **ROSS toolbox** for semi-automated spike sorting.
   * Performed automatic detection and clustering, then refined results with **manual denoising and resorting**, ending up with five distinct clusters.
   * Visualized spike waveforms, PCA plots, and spike timing on the raw signal.

3. **Single Neuron Analysis**

   * Computed **Peri-Stimulus Time Histograms (PSTHs)** to examine stimulus-specific responses.
   * Performed **Fano Factor** and **Mean-Matched Fano Factor (MMFF)** analysis to study variability.
   * Trained an **SVM classifier** on spike counts to decode stimulus categories (Face, Body, Natural, Artificial).
   * Conducted **time-time decoding** to assess sustained vs. transient neural representations.
   * Measured **Mutual Information (MI)** over time and calculated **d-prime values** for category discriminability.

4. **Population Analysis**

   * Built **Representational Dissimilarity Matrices (RDMs)** and measured alignment with ground truth categories using **Kendall’s tau correlation**.
   * Extended analysis with a **Generalized Linear Model (GLM)** combining neural RDMs and CNN-based visual features.

5. **Frequency-Based Analysis**

   * Investigated **Phase-Amplitude Coupling (PAC)** using both Modulation Index and Canolty’s method.
   * Compared PAC patterns across stimulus categories and examined spectral characteristics of neural signals.

### Summary

This assignment combined **signal processing, clustering, statistical analysis, and information-theoretic measures** to understand how neuronal activity encodes and discriminates between visual categories. The code implements a full pipeline from spike detection and sorting to higher-level decoding and representational analysis.
