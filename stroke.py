import streamlit as st
import pickle
import numpy as np

    
try:
    with open('stroke.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()
    
st.title('Stroke')
    

age = st.number_input('Age :')
bmi = st.number_input('BMI :')
avg_glucose_level = st.number_input('Avg Glucose Level :')

gender = st.selectbox('Gender',['Male','Female'])
gender_map = {'Male':1, 'Female':0}

Hypertension = st.selectbox('Hypertension',['Yes','No'])
Hypertension_map = {'Yes':1, 'No':0}

Heart_disease = st.selectbox('Heart disease',['Yes','No'])
Heart_disease_map = {'Yes':1, 'No':0}

Ever_Maried = st.selectbox('Ever Maried',['Yes','No'])
Ever_Maried_map = {'Yes':1, 'No':0}

Residense_type = st.selectbox('Residense type',['Urban','Rural'])
Residense_type_map = {'Urban':1, 'Rural':0}

smoking_status = st.selectbox('Smoking Status',['Unknown','Formerly','Never_smoked','Smoke'])
smoking_status_map = {'Unknown':0, 'Formerly':1, 'Never_smoked':2 ,'Smoke':3}

Work_Type = st.selectbox('Work Type',['Gov Job','Never Worked','Private','Self emp','Children',])
Work_Type_map = {'Gov Job':0, 'Never Worked':1, 'Private':2 ,'Self emp':3, 'Children':4}

gender_encoded = gender_map[gender]
married_encoded = Ever_Maried_map[Ever_Maried]
heart_disease_encoded = Heart_disease_map[Heart_disease]
hypertension_encoded = Hypertension_map[Hypertension]
residence_encoded = Residense_type_map[Residense_type]
smoking_encoded = smoking_status_map[smoking_status]
work_type_encoded = Work_Type_map[Work_Type]

input_data = np.array([[
    gender_encoded,        # gender
    age,                   # age
    hypertension_encoded,  # hypertension
    heart_disease_encoded, # heart_disease
    married_encoded,       # ever_married
    work_type_encoded,     # work_type
    residence_encoded,     # Residence_type
    avg_glucose_level,     # avg_glucose_level
    bmi,                   # bmi
    smoking_encoded        # smoking_status
]])

st.write("Encoded input to model:", input_data)

print()

if st.button('Predict'):
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("🚨 High risk of stroke detected. Please consult a doctor.")
    else:
        st.success("✅ No stroke risk detected. Keep maintaining a healthy lifestyle!")