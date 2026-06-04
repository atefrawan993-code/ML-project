# Student depression prediction

Student Depression Prediction — ML Project
This project uses machine learning to predict depression among students based on academic, lifestyle, and psychological factors. The dataset contains ~27,855 student records with features such as academic pressure, CGPA, sleep duration, dietary habits, financial stress, suicidal thoughts history, work/study hours, and family mental health history.

The pipeline covers:

Data Cleaning — filtering student-only records, removing invalid ages, CGPA outliers, and bad city entries.
Exploratory Data Analysis (EDA) — visualizing how factors like sleep, academic pressure, and suicidal thoughts relate to depression rates.
Feature Engineering — encoding categorical variables and creating a composite Total_Stress feature.
Modeling — training a Random Forest classifier with hyperparameter tuning via GridSearchCV (5-fold cross-validation) to predict whether a student is depressed (binary: 0/1).
Feature Importance — CGPA, age, total stress, and work/study hours were found to be the strongest predictors.
