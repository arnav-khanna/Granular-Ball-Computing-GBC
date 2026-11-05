# GBC Experimental Roadmap

An incremental roadmap for implementing, visualising, and evaluating Granular Ball Computing (GBC).

## Phase 1 — Environment & Project Setup

- [x] Set up the Python development environment.
- [x] Install dependencies:
  - [x] NumPy
  - [x] Pandas
  - [x] Matplotlib
  - [x] Scikit-learn
  - [x] SciPy
- [x] Establish the initial project directory structure.
- [x] Create a requirements.txt file.

## Phase 2 — Basic Granular Ball Computing Implementation

- [ ] Define a basic Granular Ball data structure.
  - [ ] Store the samples belonging to each ball.
  - [ ] Calculate the centre of each ball.
  - [ ] Calculate the radius of each ball.
  - [ ] Track the class distribution within each ball.
  - [ ] Calculate ball purity.

- [ ] Implement initial granular ball generation.
  - [ ] Initialise one large granular ball containing the entire dataset.
  - [ ] Implement a function to split a granular ball into smaller balls.
  - [ ] Use Scikit-learn's built-in K-Means clustering for splitting.
  - [ ] Assign samples to their respective child balls.

- [ ] Implement recursive granular ball splitting.
  - [ ] Calculate the purity of each ball.
  - [ ] Split balls whose purity is below 0.95.
  - [ ] Continue splitting until the purity threshold is satisfied.
  - [ ] Handle edge cases where further splitting is not possible.
  - [ ] Store parent-child relationships between granular balls.

## Phase 3 — Initial Dataset & Visualisation

- [ ] Generate a synthetic dataset using `sklearn.datasets.make_moons`.
- [ ] Introduce configurable noise and sample sizes.
- [ ] Run the GBC implementation on the generated dataset.
- [ ] Visualise the original dataset.
- [ ] Visualise the generated granular balls.
  - [ ] Display ball centres.
  - [ ] Display ball boundaries/radii.
  - [ ] Colour-code balls according to their dominant class.
  - [ ] Display individual data points.
- [ ] Visualise the splitting process and resulting hierarchy.
- [ ] Verify that ball purity meets the specified threshold wherever splitting is feasible.

## Phase 4 — GBKNN vs KNN Evaluation

- [ ] Implement a basic K-Nearest Neighbours (KNN) baseline using Scikit-learn.
- [ ] Implement Granular Ball K-Nearest Neighbours (GBKNN).
- [ ] Define the GBKNN prediction mechanism.
  - [ ] Determine how granular ball centres are used during neighbour selection.
  - [ ] Explore the role of ball radii in distance calculations.
  - [ ] Determine how class distributions within balls influence predictions.
- [ ] Evaluate both algorithms on the same dataset.
- [ ] Compare:
  - [ ] Classification accuracy.
  - [ ] Precision, recall and F1-score.
  - [ ] Training time.
  - [ ] Prediction time.
  - [ ] Model size / number of representative points.
- [ ] Visualise and compare decision boundaries.
- [ ] Document observations and performance differences.

## Phase 5 — Real-World Dataset Evaluation

- [ ] Introduce the Breast Cancer Wisconsin dataset using `sklearn.datasets.load_breast_cancer`.
- [ ] Perform exploratory data analysis.
- [ ] Preprocess and standardise features.
- [ ] Create training and testing splits.
- [ ] Train the GBC implementation.
- [ ] Evaluate GBKNN and conventional KNN.
- [ ] Compare results using consistent evaluation metrics.
- [ ] Investigate the effect of different purity thresholds.
- [ ] Document results and limitations.

## Phase 6 — Experimentation & Optimisation

- [ ] Experiment with different purity thresholds (0.80, 0.85, 0.90, 0.95, 0.99).
- [ ] Investigate different K-Means initialisation strategies.
- [ ] Experiment with different numbers of clusters during splitting.
- [ ] Analyse the effect of dataset size and dimensionality.
- [ ] Investigate alternative granular ball splitting strategies.
- [ ] Explore methods to reduce unnecessary granular ball generation.
- [ ] Benchmark against additional conventional machine learning algorithms.

---

## Initial Success Criteria

The first working prototype should be able to:

1. Accept a labelled dataset.
2. Initialise a single granular ball containing all samples.
3. Recursively split impure balls using K-Means.
4. Stop splitting when ball purity reaches at least 0.95, subject to valid stopping conditions.
5. Visualise the resulting granular ball structure.
6. Compare GBKNN against conventional KNN on the same dataset.

**Initial benchmark datasets:**
- `make_moons` — synthetic, two-dimensional visualisation and testing.
- `load_breast_cancer` — real-world binary classification benchmark.

**Primary objective:** Establish a working, reproducible GBC implementation before exploring more sophisticated granular ball generation, classification, and optimisation techniques.