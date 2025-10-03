# Assignment 1 - Face Identity & Spatial Frequency

The goal of the project was to investigate **how spatial frequency affects face identity recognition**. To do this, we designed and implemented a **psychophysics experiment** with morphed face images filtered at three frequency levels: intact, low, and high.

## What I Did

1. **Stimuli Preparation**

   * Created morphed face images between pairs of male and female identities.
   * Applied **low-pass** and **high-pass filters** to generate three sets of stimuli (intact, low-frequency, high-frequency).

2. **Experiment Design**

   * Built a recognition task with **1344 trials** (42 images × 32 repetitions).
   * Trials were divided into 4 blocks: three “same” blocks (one per frequency) and one “mix” block with all frequencies.
   * Implemented training sessions to ensure participants could recognize the base faces.
   * Randomized both block order and hand usage (left/right).

3. **Data Collection**

   * Each trial recorded stimulus properties (morph level, frequency), subject response (choice, hand, reaction time), and block type.
   * Data stored in structured tables (`subjectInfo`, `data`).

4. **Analysis**

   * **Psychometric fitting**: fitted sigmoidal functions to response data for each subject and condition.
   * Compared different models (sigmoid, Gaussian CDF) using **AIC/BIC**.
   * Tested hypotheses about:

     * sensitivity across frequency bands,
     * gender effects,
     * dominant vs. non-dominant hand,
     * left vs. right hand performance.
   * **ROC analysis**: computed area under the ROC curve (AuROC) as another measure of sensitivity, repeating the hypothesis tests.
   * Formulated and tested an **additional hypothesis** of my own.

5. **Phase Two (Extension)**

   * Implemented an experiment with **Active Appearance Models (AAMs)** as a closed-loop system.
   * Subjects guided the system toward a target identity through iterative feedback.
   * Analyzed results using **psychometric curves** and calculated **Just Noticeable Difference (JND)** values.

## Summary

This project combined **experiment design, psychophysics, and statistical modeling** to study how spatial frequency influences human face recognition. The code includes stimulus generation, experiment scripts, data handling, curve fitting, statistical analysis, and visualization of results.
