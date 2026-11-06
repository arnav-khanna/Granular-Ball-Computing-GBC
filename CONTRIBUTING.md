# Contributing to GBC

Thank you for your interest in contributing to this project! Contributions that improve the implementation, documentation, experiments, testing, or reproducibility are welcome.

Please read these guidelines before opening an issue or submitting a pull request.

## Ways to Contribute

You can contribute by:

- Reporting bugs or unexpected behaviour.
- Suggesting improvements to the GBC algorithm.
- Improving code quality, readability, or performance.
- Adding datasets and experimental evaluations.
- Improving visualisations and result reporting.
- Fixing documentation errors or adding examples.
- Adding tests for existing or new functionality.

## Before You Start

For substantial changes, open an issue first to discuss the proposed work. This helps avoid duplicated effort and gives contributors a chance to agree on the intended behaviour before implementation.

For small documentation fixes or straightforward bug fixes, you can usually proceed directly with a pull request.

## Reporting Bugs and Suggesting Features

When opening an issue, provide as much relevant information as possible.

For bug reports, include:

- A clear description of the problem.
- The steps required to reproduce it.
- The expected behaviour and the actual behaviour.
- Relevant error messages or logs.
- Your Python version, operating system, and relevant package versions.
- A small reproducible example or dataset, where practical.

For feature requests, explain the problem the feature would solve and describe the proposed behaviour. For algorithmic changes, include the reasoning behind the change and, where possible, supporting references or experimental evidence.

## Development Guidelines

Please follow these principles when contributing code:

1. Keep changes focused. A pull request should address one main issue or introduce one clearly defined improvement.
2. Preserve reproducibility. Keep experiments deterministic where possible. If randomness is used, expose or document the random seed.
3. Document algorithmic changes. Explain changes to splitting criteria, purity calculations, ball construction, stopping conditions, or other core GBC behaviour.
4. Avoid data leakage. Do not use class labels to determine spatial clusters or make feature-space splitting decisions unless the experiment explicitly studies a label-informed method. Clearly document any such exception.
5. Keep terminology consistent. Use the same definitions for granular balls, centres, radii, membership purity, and geometric purity throughout the code and documentation.
6. Handle edge cases. Consider empty clusters, singleton balls, identical points, non-finite values, and datasets with imbalanced classes.
7. Keep visualisation separate from algorithm logic. Plotting and result-formatting code should not unnecessarily alter the behaviour of the GBC implementation.

Follow the existing code style and structure wherever possible. Use descriptive variable and function names, add comments where the reasoning is not obvious, and avoid unrelated formatting changes.

## Experiments and Results

Contributions that add or modify experiments should make the results reproducible.

Where applicable, include:

- Dataset name and source.
- Dataset size and relevant preprocessing steps.
- Algorithm parameters and stopping conditions.
- Random seed.
- Python and dependency versions.
- Evaluation metrics and their definitions.
- The command or instructions needed to reproduce the experiment.
- Generated result files and figures, if they are part of the contribution.

Clearly distinguish between:

- Membership purity: the class composition of the samples assigned to a granular ball.
- Geometric purity: the class composition of all dataset samples that fall geometrically inside the ball's boundary.

Do not present these metrics as interchangeable. If a new metric is introduced, define exactly how it is calculated.

Do not modify reported experimental results manually. Results should be generated from the implementation, and any change in the output should be explainable by the corresponding code or configuration change.

## Testing

Before submitting a pull request:

- Run the relevant existing tests, if available.
- Run the affected experiment or provide a reproducible example.
- Check that every input sample is handled as intended.
- Check that granular-ball centres and radii are calculated correctly.
- Check that stopping conditions behave as expected.
- Check that visualisations and generated result files are produced correctly, where applicable.

If you add a new feature or fix a bug, add or update tests where practical. Include the test command and its outcome in your pull request description.

## Pull Request Process

1. Fork the repository.
2. Create a branch for your contribution.
3. Make your changes in that branch.
4. Test the changes and review the generated output.
5. Update relevant documentation.
6. Commit your changes with a clear, descriptive commit message.
7. Open a pull request against the repository's main development branch.

In your pull request description, include:

- A summary of the changes.
- The issue being addressed, if applicable.
- The reasoning behind any algorithmic or experimental changes.
- Tests or experiments performed and their results.
- Any changes to parameters, dependencies, outputs, or documented behaviour.

Keep pull requests focused and provide enough information for someone else to review and reproduce your work.

## Documentation and Figures

Use Markdown for project documentation. Keep image paths relative to the Markdown file so that figures render correctly on GitHub.

For example, if the Markdown file and image are in the same directory:

```
![Experiment results](./figure_make_moons.png)
```

If you add a generated figure, include the corresponding generation or saving step in the code where appropriate. Avoid committing temporary files, local environment folders, caches, or unrelated generated outputs.

## Code of Conduct

Be respectful and constructive when communicating with other contributors. Critique ideas and implementations, not individuals. Harassment, discriminatory language, and disruptive behaviour are not acceptable.

## Questions

If you are unsure whether a proposed change fits the project's direction, open an issue to discuss it before investing significant development effort.

Thank you for helping improve GBC!
