# Principles of Cognitive Science

This portfolio represents a series of hands-on projects completed for a university course, providing practical experience with the core tools and analytical techniques used in modern cognitive neuroscience research.

## 1. Facial Perception & Psychophysics
*   **Objective:** To investigate how different spatial frequencies in images affect our ability to recognize facial identity.
*   **Key Activities:**
    *   Designed and analyzed a psychophysical task where participants identified morphed faces filtered to contain only high, low, or intact spatial frequencies.
    *   Fit psychometric functions (sigmoidal and Gaussian CDF) to behavioral data to model perceptual sensitivity.
    *   Compared subject sensitivity using metrics like the Area under the Receiver Operating Characteristic (AuROC).
    *   Tested hypotheses on factors influencing identity detection (e.g., gender of subject/stimulus, hand dominance).
    *   **Advanced Extension:** Used Active Appearance Models (AAMs) to generate a continuum of faces and designed a closed-loop experiment to study the perceptual trajectory between identities.

## 2. Neural Data Analysis & Electrophysiology
*   **Objective:** To process and interpret neural signals, from single neurons to large populations, to understand visual coding.
*   **Key Activities:**
    *   **Spike Sorting:** Built a processing pipeline from scratch to isolate individual neuron activity from raw extracellular recordings, involving filtering, spike detection, feature extraction (PCA, t-SNE), and clustering (K-Means). Also utilized the ROSS software for automated sorting.
    *   **Single Neuron Analysis:** Analyzed data from the macaque Inferior Temporal (IT) cortex.
        *   Calculated Peri-Stimulus Time Histograms (PSTHs) to visualize response profiles to different visual categories (Faces, Bodies, Natural, Artificial objects).
        *   Quantified neural variability using the Mean-Matched Fano Factor.
        *   Used Mutual Information and d-prime metrics to assess a neuron's selectivity and discriminability between categories.
    *   **Population-Level Decoding:**
        *   Employed Support Vector Machines (SVM) to decode stimulus category from neural firing patterns, including a time-time generalization analysis to track information dynamics.
        *   Constructed Representational Dissimilarity Matrices (RDMs) to study the population coding structure and its alignment with stimulus categories over time.
    *   **Phase-Amplitude Coupling (PAC):** Used the TensorPAC toolbox to investigate cross-frequency coupling in local field potentials (LFPs) across stimulus categories.

## 3. EEG Analysis of Visual Processing
*   **Objective:** To decode high-level visual category information (Faces vs. Houses) from scalp-recorded EEG signals.
*   **Key Activities:**
    *   Preprocessed raw EEG data (filtering, epoching, artifact removal, baseline correction).
    *   Analyzed Event-Related Potentials (ERPs) to identify significant differences between conditions.
    *   Conducted time-frequency analysis to study task-related oscillatory power changes.
    *   Applied Multivariate Pattern Analysis (MVPA) to decode stimulus category from spatial and temporal patterns of EEG activity.
    *   Performed Representational Similarity Analysis (RSA) to compare neural representations from EEG with those from a deep neural network model (CORnet-S), tracing the hierarchical visual processing pathway.

## 4. fMRI Data Analysis & GLM
*   **Objective:** To localize brain activity in response to visual stimuli and perform statistical inference using the General Linear Model (GLM).
*   **Key Activities:**
    *   Manipulated and visualized neuroimaging data (T1-weighted and BOLD images).
    *   Built design matrices for task-based fMRI, convolving task paradigms with hemodynamic response functions (HRF).
    *   Fit GLMs to BOLD data, both with and without confound regressors (e.g., motion parameters).
    *   Computed and visualized statistical contrast maps (Z-scores) to identify regions significantly activated by left vs. right visual field stimuli.
    *   Mapped functional activity onto anatomical regions of interest (ROIs), specifically the Lateral Geniculate Nucleus (LGN).
