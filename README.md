# NBA Next Pick


## Overview

NBA Next Pick is a machine learning project that predicts the probability of college basketball players being drafted into the NBA. By analyzing player statistics, demographics, and performance data, the project helps NBA teams make data-driven decisions during the draft process, improving scouting efficiency and talent identification.

## Project Description

### For Non-Technical Audience (e.g., HR, Stakeholders)

This project helps NBA teams make smarter decisions during the player draft by predicting how likely college basketball players are to be drafted into the NBA. Imagine a tool that analyzes player stats, performance, and other data to give each player a "draft probability" score. This allows teams to focus their time and money on scouting the most promising players, reducing wasted effort on those less likely to be drafted. The goal is to improve talent identification, build better teams, and make the draft process fairer and more efficient for everyone involved, from players to coaches to fans.

### For Technical Audience (e.g., Interviewers, Data Scientists)

This is a binary classification machine learning project aimed at predicting the probability of NBA draft selection for college basketball players. The dataset comprises player statistics, demographic information, and performance metrics from historical drafts. The project follows a structured experimental approach:

1. **Data Preprocessing and Baseline**: Initial data cleaning, feature engineering, and establishment of a Logistic Regression baseline model.
2. **Feature Selection**: Various techniques were applied for feature engineering to reduce dimensionality.
3. **Model Optimization**: Models were optimized using a combination of manual and grid search techniques, focusing on XGBoost hyperparameter tuning.
4. **Ensemble Modeling**: Combination of Logistic Regression, LDA, and XGBoost via soft voting for improved robustness and performance.

Key evaluation metrics include ROC-AUC (measuring discriminative power across probability thresholds) and Recall (ensuring high true positive rate for drafted players to minimize missed opportunities). The final ensemble model achieves ROC-AUC scores above 0.98 and Recall above 0.94 on test data, demonstrating excellent generalization and alignment with business objectives for NBA scouting efficiency.

## Installation

1. Clone the repository and navigate to the project directory.
2. Install Poetry for dependency management: `pip install poetry`.
3. Set up the virtual environment: `poetry install`.
   - **Note**: If the `doombuoy` package cannot be installed from Test PyPI, a wheel file is included in the `package/` directory and will be installed locally.
4. (Optional) Install pyenv for Python version management if needed.
5. Obtain a Kaggle API token and place it in `~/.kaggle/kaggle.json`.
6. Run the data download script: `poetry run python nba_next_pick/dataset.py`.

## Usage

1. Activate the virtual environment: `poetry shell`.
2. Launch Jupyter Lab: `poetry run jupyter lab`.
3. Open and run the experimental notebooks in the `notebooks/` directory in order (experiment-1.ipynb to experiment-4.ipynb).
4. For model training and prediction, use the scripts in `nba_next_pick/modeling/`.

## Data

The dataset is sourced from the UTS-36120-25SP Kaggle competition. It includes historical player data such as statistics, demographics, and draft outcomes. Raw data is stored in `data/raw/`, processed data in `data/processed/`.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for
│                         nba_next_pick and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── nba_next_pick   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes nba_next_pick a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py          <- Code to run model inference with trained models
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

## Experiments

The project includes four experimental notebooks that progressively build and evaluate models for predicting NBA draft probabilities.

### Experiment 1: Data Processing and Baseline Model (Logistic Regression)

This notebook handles data loading, preprocessing, feature engineering, and establishes a baseline model performance using Logistic Regression.

**Performance Metrics:**
- Training ROC-AUC: 0.9938
- Validation ROC-AUC: 0.9903
- Test ROC-AUC: 0.9769

### Experiment 2: Feature Selection with LDA

Focuses on selecting the most important features to improve model efficiency and reduce overfitting, using Linear Discriminant Analysis (LDA).

**Performance Metrics:**
- Train AUROC: 0.9838
- Validation AUROC: 0.9824
- Test AUROC: 0.9766

### Experiment 3: Hyperparameter Tuning with XGBoost

Uses XGBoost with hyperparameter tuning to optimize performance.

**Performance Metrics:**
- Train AUROC: 0.9683, Recall: 0.8966
- Validation AUROC: 0.9538, Recall: 0.9000
- Test AUROC: 0.9512, Recall: 0.8421

### Experiment 4: Ensemble Modeling

Combines Logistic Regression, LDA, and XGBoost into an ensemble using voting for improved robustness and performance.

**Performance Metrics:**
- Train AUROC: 0.9878, Recall: 1.0000
- Validation AUROC: 0.9840, Recall: 0.9474
- Test AUROC: 0.9825, Recall: 0.9474

Outcome: Alternate Hypothesis Confirmed - Ensemble models reduce overfitting and improve performance.

All experiments aim to achieve AUROC > 0.95 and high recall for the drafted class.

## Contributing

Contributions are welcome! Please follow the standard Git workflow: fork the repository, create a feature branch, and submit a pull request. Ensure code adheres to the project's linting and formatting standards (flake8, black, isort).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- Agam Singh Saini (Student ID: 25531702)

## Acknowledgments

- Based on the Cookiecutter Data Science template.
- Data sourced from Kaggle (UTS-36120-25SP competition).

