# mlops-unit1

MLOps Practice Exercises — Git, Dev & Python (Unit 1)

---

## Project Overview

This repository contains solutions to the **MLOps Practice Exercise Questions** covering Git version control, Python ML workflows, project structuring, and reproducibility.

---

## Project Structure

```
mlops-unit1/
├── Exercise 1/
│   ├── data/
│   │   └── data.csv
│   └── dataset_stats.py
├── Exercise 2/
│   ├── data/
│   │   └── data.csv
│   ├── model/
│   │   └── model.pkl
│   ├── src/
│   │   └── main.py
│   └── requirements.txt
└── README.md
```

---

## Exercise 1: Git & Version Control (MLOps Basics)

1. Created a Git repository for the ML project named `mlops-unit1`.
2. Wrote a Python script ([dataset_stats.py](dataset_stats.py)) that loads a dataset and prints basic statistics (min, max, mean) for numeric columns.
3. Committed the code with appropriate commit messages.
4. Created a branch called `experiment-v1` and made changes in the code.
5. Merged the branch back into the `main` branch.

---

## Exercise 2: Python ML Workflow

Implemented in [Exercise 2/src/main.py](Exercise%202/src/main.py):

1. **Data Loading** — Loads the dataset from `data/data.csv` using `pandas`.
2. **Data Splitting** — Splits data into training (60%) and testing (40%) sets using `train_test_split`.
3. **Model Training** — Trains a **Logistic Regression** model on features `f1` and `f2`.
4. **Evaluation** — Prints model accuracy using `sklearn.metrics.accuracy_score`.
5. **Model Saving** — Saves the trained model as `model/model.pkl` using `joblib`, then loads and verifies predictions from the saved model.

---

## Exercise 3: Dev Workflow & Project Structure

The project is organized following an MLOps-friendly folder structure:

| Folder / File | Purpose |
|---|---|
| `data/` | Contains datasets |
| `Exercise 2/src/` | Source code for ML workflow |
| `Exercise 2/model/` | Saved trained models |
| `Exercise 2/requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## Exercise 4: Reproducibility Using Python & Git

### Python Dependencies

All dependencies are listed in [Exercise 2/requirements.txt](Exercise%202/requirements.txt):

```
joblib==1.5.3
pandas==3.0.1
scikit_learn==1.8.0
```

### How to Recreate the Environment

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd mlops-unit1
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r "Exercise 2/requirements.txt"
   ```

4. **Run the dataset statistics script (Exercise 1):**
   ```bash
   python dataset_stats.py
   ```

5. **Run the ML workflow (Exercise 2):**
   ```bash
   python "Exercise 2/src/main.py"
   ```

---

## Technologies Used

- Python 3.12
- pandas
- scikit-learn
- joblib
