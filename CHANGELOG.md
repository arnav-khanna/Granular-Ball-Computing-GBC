# Changelog

## Initial Development — Environment Setup and First GBC Experiment

### 1. Development Environment
- Set up the Python development environment.
- Installed and configured the required dependencies, including NumPy, Matplotlib and Scikit-learn.
- Prepared the environment to run the initial Granular Ball Computing (GBC) experiment.

### 2. Initial GBC Implementation
- Implemented the initial Granular Ball Computing pipeline using the `make_moons` dataset.
- Generated a dataset containing 500 samples, with a noise level of 0.15 and random state 42.
- Implemented recursive spatial splitting using K-Means clustering.
- Configured K-Means to generate two clusters per split, using only feature coordinates and not class labels.
- Implemented granular-ball property calculations, including:
  - Centre calculation using the mean position of assigned samples.
  - Radius calculation using the maximum Euclidean distance from the centre.
  - Membership-purity calculation.
  - Dominant-class identification.
- Implemented recursive splitting with a membership-purity threshold of 0.95.
- Configured a minimum child size of 1 and maximum recursion depth of 100.

### 3. Results Display and Verification
*The following functionality is separate from the core GBC algorithm. The initial results-display and verification code was AI-assisted and will be independently developed in a future iteration.*

- Added terminal output displaying the properties of each final granular ball.
- Added membership-purity verification to check whether all final balls meet the configured threshold.
- Implemented sample assignment verification to check that every sample is assigned exactly once.
- Added boundary verification to check whether assigned samples lie within their respective granular-ball boundaries.
- Implemented geometric-purity verification by checking all dataset samples lying inside each granular ball's enclosing circle.
- Compared membership purity with geometric purity to investigate differences between assigned membership and the complete geometric region.

### 4. Visualisation
- Implemented a three-panel Matplotlib visualisation showing:
  - The original dataset and its two classes.
  - The GBC decomposition, including granular-ball boundaries, centres and membership-purity values.
  - Individual granular-ball membership, with separate colours for each ball.
- Displayed the visualisation using Matplotlib.
- Saved the generated figure as `figure.png`.

### 5. Experimental Results and Documentation
- Completed the initial experiment using the configured GBC implementation.
- Generated 12 final granular balls from the 500-sample dataset.
- Verified that all 12 balls reached the membership-purity threshold of 0.95.
- Confirmed that every sample was assigned exactly once.
- Confirmed that no assigned samples fell outside their respective granular-ball boundaries.
- Completed geometric-purity analysis.
- Prepared and saved results, documenting:
  - Experiment configuration.
  - Individual granular-ball statistics.
  - Membership-purity verification.
  - Sample assignment verification.
  - Boundary verification.
  - Geometric-purity results.
  - Observations, discussion and conclusion.
- Referenced the generated visualisation in the results documentation.

### 6. Initial Experiment Summary

| Metric | Result |
|---|---:|
| Dataset | `make_moons` |
| Dataset samples | 500 |
| Final granular balls | 12 |
| Purity threshold | 0.95 |
| Balls reaching membership-purity threshold | 12 / 12 |
| Sample assignment verification | Passed |
| Boundary verification | Passed |
| Geometric-purity analysis | Completed |

### 7. Current Project Status

- Development environment configured.
- Initial GBC implementation completed and executed.
- Recursive spatial K-Means splitting implemented.
- Results-display and verification functionality implemented separately from the core algorithm.
- Three-panel visualisation generated and saved as `experiments/make_moons/figure.png`.
- Experimental results documented and saved in `experiments/make_moons/README.md`.

**Current milestone:** Initial `make_moons` GBC experiment completed, visualised, verified and documented.