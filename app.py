import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Prediction of Disease Outbreaks")

# Function to load models
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Loading the saved models
dm = load_model('diabetes_model.sav')
hm = load_model('heart_disease_model.sav')
pm = load_model('parkinsons_model.sav')

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreaks System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital', icons=['activity', 'heart', 'person'], default_index=0)

# Function to get user input
def get_user_input(labels):
    user_input = []
    for label in labels:
        value = st.text_input(label, '0')
        user_input.append(float(value))
    return user_input

# Function to display prediction results
def display_result(prediction, positive_msg, negative_msg):
    if prediction[0] == 1:
        st.success(positive_msg)
    else:
        st.success(negative_msg)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    labels = ['Number of Pregnancies', 'Glucose Level', 'Blood Pressure value', 'Skin Thickness value',
              'Insulin Level', 'BMI value', 'Diabetes Pedigree Function value', 'Age of the Person']
    col1, col2 = st.columns(2)
    with col1:
        user_input = get_user_input(labels[:4])
    with col2:
        user_input.extend(get_user_input(labels[4:]))
    if st.button('Diabetes Test Result'):
        diab_prediction = dm.predict([user_input])
        display_result(diab_prediction, 'The person is diabetic', 'The person is not diabetic')

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    labels = ['Age', 'Sex', 'Chest Pain types', 'Resting Blood Pressure', 'Serum Cholestoral in mg/dl',
              'Fasting Blood Sugar > 120 mg/dl', 'Resting Electrocardiographic results', 'Maximum Heart Rate achieved',
              'Exercise Induced Angina', 'ST depression induced by exercise', 'Slope of the peak exercise ST segment',
              'Major vessels colored by flourosopy', 'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect']
    col1, col2 = st.columns(2)
    with col1:
        user_input = get_user_input(labels[:7])
    with col2:
        user_input.extend(get_user_input(labels[7:]))
    if st.button('Heart Disease Test Result'):
        heart_prediction = hm.predict([user_input])
        display_result(heart_prediction, 'The person is having heart disease', 'The person does not have any heart disease')

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    labels = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ',
              'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA',
              'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE']
    col1, col2, col3 = st.columns(3)
    with col1:
        user_input = get_user_input(labels[:8])
    with col2:
        user_input.extend(get_user_input(labels[8:16]))
    with col3:
        user_input.extend(get_user_input(labels[16:]))
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = pm.predict([user_input])
        display_result(parkinsons_prediction, "The person has Parkinson's disease", "The person does not have Parkinson's disease")
