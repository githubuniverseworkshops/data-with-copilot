# Data Transformation CLI

This project provides a command-line interface (CLI) for transforming a dataset stored in a CSV file. The transformations include dropping columns, selecting high ratings, one-hot encoding, removing newlines and carriage returns, and converting ratings to integers.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Transformations](#data-transformations)
- [Testing](#testing)
- [GitHub Actions](#github-actions)
- [License](#license)
- [Code of Conduct](#code-of-conduct)

## Overview

This project is designed to help you manipulate and clean a dataset using a series of predefined functions. The CLI allows you to apply these transformations to your data and save the results.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Set up a virtual environment and install dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate
    pip install -r workshop/requirements.txt
    ```

## Usage

To use the CLI, run the `main.py` script with the desired command:

```sh
python main.py run_all
```

## Data Transformations
The following transformations are applied to the dataset:

* Drop Notes: Removes the 'notes' column.
* Select High Ratings: Filters rows where the 'rating' is 90 or higher.
* One-Hot Encode Red Wine: Creates a 'Red_Wine' column and drops the 'variety' column.
* Remove Newlines and Carriage Returns: Cleans string columns by removing newlines and carriage returns.
* Convert Ratings to Int: Converts the 'rating' column from float to integer.

## Data Transformations

To run the tests, use the following command:

```shell
pytest test_main.py
```

## GitHub Actions

This project includes a GitHub Action workflow to automate the data transformation process. The workflow is defined in .github/workflows/transform-data.yaml and runs on every push to the main branch, pull requests, and manual dispatch.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Code of Conduct

This project adheres to a Code of Conduct. By participating, you are expected to uphold this code.

Feel free to contribute to this project by opening issues or submitting pull requests. If you have any questions, please contact the repository owner.