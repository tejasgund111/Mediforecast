import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime
from streamlit_option_menu import option_menu


# loading the saved models
diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('saved_models/parkinsons_model.sav', 'rb'))


# Template for Diabetes
def diabetes_template():
    st.write("# Diabetes Prediction")
    col1, col2 = st.columns(2)
    with col1:
        st.image("diabetes3.jpg", width=300, output_format="JPG", use_column_width=True, clamp=True)
    with col2:
        st.image("diabetes4.jpg", width=300, output_format="JPG", use_column_width=True, clamp=True)
    st.write("""
    Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces. Insulin is a hormone that regulates blood sugar. Hyperglycemia, or raised blood sugar, is a common effect of uncontrolled diabetes and, over time, leads to serious damage to many of the body's systems.
    """)

    # Apply CSS styling for rounded corners
    st.markdown(
        """
        <style>
            img {
                border-radius: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def heart_disease_template():
    st.write("# Heart Disease Prediction")
    col1, col2 = st.columns(2)
    with col1:
        st.image("heart1.jpeg", width=300, output_format="JPEG", use_column_width=True, clamp=True)
    with col2:
        st.image("heart2.jpg", width=300, output_format="JPG", use_column_width=True, clamp=True)
    st.write("Heart disease refers to several types of heart conditions. The most common type of heart disease in the United States is coronary artery disease, which affects the blood flow to the heart. Reduced blood flow can cause chest pain (angina), heart attack, heart failure, and arrhythmias.")
    # Apply CSS styling for rounded corners
    st.markdown(
        """
        <style>
            img {
                border-radius: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def parkinsons_template():
    st.write("# Parkinson's Disease Prediction")
    st.image("parkinsons1.jpeg", width=300)
    st.write("Parkinson's disease is a progressive nervous system disorder that affects movement. Symptoms start gradually, sometimes starting with a barely noticeable tremor in just one hand. Tremors are common, but the disorder also commonly causes stiffness or slowing of movement.")
    # Apply CSS styling for rounded corners
    st.markdown(
        """
        <style>
            img {
                border-radius: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )



# Function to get user inputs for patient information
def page_patient_info():
    # st.subheader("Patient Information")
    name = st.text_input("Name")
    mobile_number = st.text_input("Mobile Number")
    gender = st.selectbox("Gender", ["Male", "Female"])
    return name, mobile_number, gender

# Function to get user inputs for each disease prediction
def page_select_disease():
    # st.subheader("Select Disease")
    selected_disease = st.selectbox("Select Disease", ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"])
    return selected_disease

def get_patient_info():
    st.sidebar.subheader("Patient Information")
    name = st.sidebar.text_input("Name")
    mobile_number = st.sidebar.text_input("Mobile Number")
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    return name, mobile_number, gender

# Function to get user inputs for each disease prediction
def get_diabetes_input():
    # st.subheader("Diabetes Prediction")
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=17, value=0, step=1)
    glucose = st.number_input("Glucose Level", min_value=0, value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, value=0)
    insulin = st.number_input("Insulin Level", min_value=0, value=0)
    bmi = st.number_input("BMI", min_value=0.0, value=0.0)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.0)
    age = st.number_input("Age", min_value=0, value=0)
    return [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]

# Validation and conversion of the input to float values
def validate_and_convert_input(input_str, default_value=0.0):
    try:
        return float(input_str)
    except ValueError:
        return default_value

# Function to get heart disease input and convert to float
def get_heart_disease_input():
    age = validate_and_convert_input(st.text_input("Age"))
    sex = validate_and_convert_input(st.selectbox("Sex (1 = male; 0 = female)", [1, 0]))
    cp = validate_and_convert_input(st.text_input("Chest Pain Type (0-3)"))
    trestbps = validate_and_convert_input(st.text_input("Resting Blood Pressure"))
    chol = validate_and_convert_input(st.text_input("Serum Cholestoral in mg/dl"))
    fbs = validate_and_convert_input(st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)", [1, 0]))
    restecg = validate_and_convert_input(st.text_input("Resting Electrocardiographic Results (0-2)"))
    thalach = validate_and_convert_input(st.text_input("Maximum Heart Rate Achieved"))
    exang = validate_and_convert_input(st.selectbox("Exercise Induced Angina (1 = yes; 0 = no)", [1, 0]))
    oldpeak = validate_and_convert_input(st.text_input("ST Depression Induced by Exercise"))
    slope = validate_and_convert_input(st.text_input("Slope of the Peak Exercise ST Segment (0-2)"))
    ca = validate_and_convert_input(st.text_input("Number of Major Vessels (0-3) Colored by Flourosopy"))
    thal = validate_and_convert_input(st.selectbox("Thal (1 = normal; 2 = fixed defect; 3 = reversable defect)", [1, 2, 3]))

    return [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]


def get_parkinsons_input():
    # st.subheader("Parkinson's Disease Prediction")
    features = [
        "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)",
        "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)", "Shimmer:APQ3",
        "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR", "RPDE", "DFA", "spread1", "spread2",
        "D2", "PPE"
    ]
    inputs = []
    for feature in features:
        value = st.number_input(feature)
        inputs.append(value)
    return inputs

# Function to view patient information
def page_view_patient_info():
    # st.subheader("View Patient Information")
    view_key = st.text_input("Enter View Key", type="password")
    if view_key == "viewkey":
        show_data = st.checkbox("Show Patient Data")
        if show_data:
            df = pd.read_csv("patient_info.csv")
            st.subheader("Patient Information")
            st.write(df)

# Function to display prediction result
def display_prediction_result(prediction):
    if prediction == 1:
        st.success("Positive Prediction")
    else:
        st.success("Negative Prediction")

# Function to collect feedback
def collect_feedback():
    st.title("Feedback")
    feedback = st.text_area("Please leave your feedback here:")
    if st.button("Submit Feedback"):
        if feedback:
            feedback_df = pd.DataFrame({"Feedback": [feedback], "Timestamp": [datetime.now()]})
            feedback_df.to_csv("feedback.csv", mode="a", header=False, index=False)
            st.success("Thank you for your feedback!")
        else:
            st.warning("Please provide your feedback before submitting.")

# Main function to run the app
def main():
    st.sidebar.title("Navigation")
    with st.sidebar:
        selected_page = option_menu('MediForecast',
                                    ['Home',
                                     'Patient Information',
                                     'Prediction',
                                     'View Patient Information',
                                     'Feedback'],
                                    icons=['house-heart-fill','bi-person-add','bi-person-raised-hand','bi-person-lock','bi-person-rolodex'],
                                    menu_icon='heart-eyes-fill',
                                    default_index=0)




    if selected_page == "Home":
        st.title("Home")
        # Add content for the home page here
        st.write("Welcome to our Health Prediction App!")

        st.write("### Choose a Disease to Learn More and Make Predictions")

        # Disease selection
        selected_disease = st.selectbox("Select Disease", ["Diabetes", "Heart Disease", "Parkinson's Disease"])

        if selected_disease == "Diabetes":
            diabetes_template()
        elif selected_disease == "Heart Disease":
            heart_disease_template()
        elif selected_disease == "Parkinson's Disease":
            parkinsons_template()

    elif selected_page == "Patient Information":
        st.title("Patient Information")
        name, mobile_number, gender = page_patient_info()
        if st.button("Submit"):
            if not name or not mobile_number or not gender:
                st.error("Please fill in all fields.")
            else:
                # Store patient information
                st.success("Patient information submitted successfully!")
                # Save patient information to CSV

    elif selected_page == "Prediction":
        st.title("Prediction")
        selected_disease = page_select_disease()

        if selected_disease == "Diabetes Prediction":
            st.title('Diabetes Prediction')
            patient_name, mobile_number, gender = get_patient_info()
            user_input = get_diabetes_input()
            if st.button("Predict Diabetes"):
                prediction = diabetes_model.predict([user_input])
                display_prediction_result(prediction)
                # Save prediction result to CSV
                df = pd.read_csv("patient_info.csv")
                new_row = {"Name": patient_name, "Mobile Number": mobile_number, "Gender": gender, 
                        "Diabetes Prediction": prediction[0], "Heart Disease Prediction": np.nan, 
                        "Parkinson's Prediction": np.nan, "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                df.to_csv("patient_info.csv", index=False)
                
        elif selected_disease == "Heart Disease Prediction":
            st.title('Heart Disease Prediction')
            patient_name, mobile_number, gender = get_patient_info()
            user_input = get_heart_disease_input()
            if st.button("Predict Heart Disease"):
                prediction = heart_disease_model.predict([user_input])
                display_prediction_result(prediction)
                # Save prediction result to CSV
                df = pd.read_csv("patient_info.csv")
                new_row = {"Name": patient_name, "Mobile Number": mobile_number, "Gender": gender, 
                           "Diabetes Prediction": np.nan, "Heart Disease Prediction": prediction[0], 
                           "Parkinson's Prediction": np.nan, "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                df.to_csv("patient_info.csv", index=False)
                
        elif selected_disease == "Parkinson's Prediction":
            st.title("Parkinson's Disease Prediction")
            patient_name, mobile_number, gender = get_patient_info()
            user_input = get_parkinsons_input()
            if st.button("Predict Parkinson's Disease"):
                prediction = parkinsons_model.predict([user_input])
                display_prediction_result(prediction)
                # Save prediction result to CSV
                df = pd.read_csv("patient_info.csv")
                new_row = {"Name": patient_name, "Mobile Number": mobile_number, "Gender": gender, 
                           "Diabetes Prediction": np.nan, "Heart Disease Prediction": np.nan, 
                           "Parkinson's Prediction": prediction[0], "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                df.to_csv("patient_info.csv", index=False)
    
    elif selected_page == "View Patient Information":
        st.title("View Patient Information")
        page_view_patient_info()

    elif selected_page == "Feedback":
        collect_feedback()

if __name__ == "__main__":
    main()

