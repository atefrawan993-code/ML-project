import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('depression_model.pkl')

# App Title
st.title('Student Depression Prediction')
st.write('Fill in the information below to predict if a student is at risk of depression.')

# Input Fields
age = st.slider('Age', min_value=15, max_value=40, value=20)

gender = st.selectbox('Gender', ['Male', 'Female'])
gender_encoded = 1 if gender == 'Female' else 0

cgpa = st.slider('CGPA', min_value=0.0, max_value=10.0, value=7.0, step=0.1)

academic_pressure = st.slider('Academic Pressure (1-5)', min_value=1, max_value=5, value=3)

work_study_hours = st.slider('Work/Study Hours per Day', min_value=0, max_value=16, value=6)

financial_stress = st.slider('Financial Stress (1-5)', min_value=1, max_value=5, value=3)

total_stress = academic_pressure + financial_stress

# Predict Button
if st.button('Predict'):
    input_data = np.array([[age, cgpa, academic_pressure,
                            work_study_hours, financial_stress,
                            total_stress, gender_encoded]])
    
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error(' This student is likely at risk of depression.')
    else:
        st.success('This student is not at risk of depression.')
