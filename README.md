# 🎓 Student Depression Prediction — Machine Learning Project
 
A machine learning project that predicts depression among students based on academic, lifestyle, and psychological factors. The goal is to identify at-risk students early using data-driven insights.
 
---
 
## 📋 Table of Contents
 
- [Overview](#overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Workflow](#workflow)
- [Models & Results](#models--results)
- [Feature Importance](#feature-importance)
- [Key Findings](#key-findings)
- [Technologies Used](#technologies-used)
---
 
## Overview
 
Mental health among students is a growing concern. This project builds a binary classification model to predict whether a student is depressed (1) or not (0), using features such as academic pressure, CGPA, sleep habits, financial stress, and more.
 
---
 
## Dataset
 
- **Source:** Student Depression Dataset (CSV)
- **Size:** ~27,855 student records (after cleaning)
- **Target Variable:** `Depression` (0 = Not Depressed, 1 = Depressed)
### Features
 
| Feature | Description |
|---|---|
| Age | Student's age |
| Gender | Male / Female |
| CGPA | Academic grade point (0–10) |
| Academic Pressure | Self-reported pressure score |
| Study Satisfaction | Satisfaction with studies |
| Sleep Duration | Hours of sleep per night |
| Dietary Habits | Healthy / Moderate / Unhealthy |
| Work/Study Hours | Daily hours spent working or studying |
| Financial Stress | Financial stress level |
| Suicidal Thoughts | Whether the student has had suicidal thoughts |
| Family History of Mental Illness | Family mental health background |
 
---
 
## Project Structure
 
```
├── ML_Student_Depression_project.ipynb   # Main notebook
├── Student Depression Dataset.csv        # Raw dataset
├── depression_model.pkl                  # Saved trained model
└── README.md
```
 
---
 
## Installation
 
1. Clone or download the repository.
2. Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
 
3. Open the notebook in Jupyter or Google Colab and run all cells.
---
 
## Workflow
 
### Phase 1 — Data Cleaning
- Filtered to student-only records
- Removed invalid city entries and impossible age/CGPA values
- Dropped rows with missing age values
### Phase 2 — Exploratory Data Analysis (EDA)
Key questions explored:
- Do students with suicidal thoughts have higher depression rates?
- Does sleep duration affect depression?
- How does academic pressure distribute across the dataset?
### Phase 3 — Feature Engineering
- Encoded categorical variables (Gender, Sleep Duration, Dietary Habits, etc.)
- Created a composite `Total_Stress` feature combining academic, financial, and work pressure
### Phase 4 — Modeling
- Split data: **80% training / 20% testing**
- Trained and compared four models
- Used **GridSearchCV with 5-fold cross-validation** for hyperparameter tuning
### Phase 5 — Evaluation
- Evaluated models using **Precision** and **Recall**
- Analyzed feature importances from the best model
---
 
## Models & Results
 
| Model | Precision | Recall |
|---|---|---|
| Logistic Regression | 0.798 | 0.837 |
| Decision Tree | 0.740 | 0.744 |
| Random Forest | 0.781 | 0.811 |
| **Tuned Random Forest** ✅ | **0.790** | **0.846** |
 
The **Tuned Random Forest** achieved the best overall performance with the following optimal hyperparameters:
 
```
n_estimators: 50
max_depth: 5
min_samples_split: 2
```
 
The trained model is saved as `depression_model.pkl` for future use.
 
---
 
## Feature Importance
 
The top predictors of student depression identified by the model:
 
| Rank | Feature | Importance |
|---|---|---|
| 1 | CGPA | 0.317 |
| 2 | Age | 0.174 |
| 3 | Total Stress | 0.168 |
| 4 | Work/Study Hours | 0.139 |
| 5 | Academic Pressure | 0.118 |
| 6 | Financial Stress | 0.061 |
| 7 | Gender | 0.024 |
 
---
 
## Key Findings
 
- Students with **suicidal thoughts** show significantly higher depression rates.
- **Poor sleep** (less than 5 hours) is strongly associated with depression.
- **High academic pressure** combined with low study satisfaction increases depression risk.
- **CGPA** is the single strongest predictor — both very low and certain high-stress academic profiles correlate with depression.
---
 
## Technologies Used
 
- **Python 3**
- **Pandas** — data manipulation
- **NumPy** — numerical operations
- **Matplotlib & Seaborn** — data visualization
- **Scikit-learn** — machine learning models, GridSearchCV, evaluation metrics

## link of video presentation 
https://drive.google.com/file/d/10tOsm3Znxb2M-pWJIFChtnw8Z-Z3XniU/view?usp=sharing

## link of  live app
https://student-depression-prediction-ml.streamlit.app
