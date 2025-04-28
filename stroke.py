import streamlit as st
import pickle
import numpy as np

# Load model
try:
    with open('stroke.pkl', 'rb') as f:
        model = pickle.load(f)
    st.success("Model loaded successfully! Ready to predict.")
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()

st.title('Stroke Prediction App')

# Input Fields
age = st.number_input('Age :')
bmi = st.number_input('BMI :')
avg_glucose_level = st.number_input('Avg Glucose Level :')

gender = st.selectbox('Gender', ['Male', 'Female'])
gender_map = {'Male': 1, 'Female': 0}

hypertension = st.selectbox('Hypertension', ['Yes', 'No'])
hypertension_map = {'Yes': 1, 'No': 0}

heart_disease = st.selectbox('Heart Disease', ['Yes', 'No'])
heart_disease_map = {'Yes': 1, 'No': 0}

ever_married = st.selectbox('Ever Married', ['Yes', 'No'])
ever_married_map = {'Yes': 1, 'No': 0}

residence_type = st.selectbox('Residence Type', ['Urban', 'Rural'])
residence_type_map = {'Urban': 1, 'Rural': 0}

smoking_status = st.selectbox('Smoking Status', ['Unknown', 'Formerly smoked', 'Never smoked', 'Smokes'])
smoking_status_map = {'Unknown': 0, 'Formerly smoked': 1, 'Never smoked': 2, 'Smokes': 3}

work_type = st.selectbox('Work Type', ['Govt Job', 'Never Worked', 'Private', 'Self-employed', 'Children'])
work_type_map = {'Govt Job': 0, 'Never Worked': 1, 'Private': 2, 'Self-employed': 3, 'Children': 4}

# Encoding Inputs
encoded_inputs = {
    'gender': gender_map[gender],
    'ever_married': ever_married_map[ever_married],
    'heart_disease': heart_disease_map[heart_disease],
    'hypertension': hypertension_map[hypertension],
    'residence_type': residence_type_map[residence_type],
    'smoking_status': smoking_status_map[smoking_status],
    'work_type': work_type_map[work_type]
}

# Prepare data for prediction
input_data = np.array([[
    encoded_inputs['gender'],
    age,
    encoded_inputs['hypertension'],
    encoded_inputs['heart_disease'],
    encoded_inputs['ever_married'],
    encoded_inputs['work_type'],
    encoded_inputs['residence_type'],
    avg_glucose_level,
    bmi,
    encoded_inputs['smoking_status']
]])

st.write("Encoded input to model:", input_data)

# Prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("🚨 High risk of stroke detected. Please consult a doctor.")
    else:
        st.success("✅ No stroke risk detected. Keep maintaining a healthy lifestyle!")
