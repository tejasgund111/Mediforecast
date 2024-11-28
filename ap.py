# import streamlit as st
# import pandas as pd
# import numpy as np
# import pickle

# # loading the saved models
# diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))
# heart_disease_model = pickle.load(open('saved_models/heart_disease_model.sav', 'rb'))
# parkinsons_model = pickle.load(open('saved_models/parkinsons_model.sav', 'rb'))

# # Function to get user inputs for patient information
# def get_patient_info():
#     st.sidebar.subheader("Patient Information")
#     name = st.sidebar.text_input("Name")
#     mobile_number = st.sidebar.text_input("Mobile Number")
#     gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
#     return name, mobile_number, gender

# # Function to get user inputs for each disease prediction
# def get_diabetes_input():
#     st.subheader("Diabetes Prediction")
#     pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=17, value=0, step=1)
#     glucose = st.number_input("Glucose Level", min_value=0, value=0)
#     blood_pressure = st.number_input("Blood Pressure", min_value=0, value=0)
#     skin_thickness = st.number_input("Skin Thickness", min_value=0, value=0)
#     insulin = st.number_input("Insulin Level", min_value=0, value=0)
#     bmi = st.number_input("BMI", min_value=0.0, value=0.0)
#     diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.0)
#     age = st.number_input("Age", min_value=0, value=0)
#     return [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]

# def get_heart_disease_input():
#     st.subheader("Heart Disease Prediction")
#     age = st.number_input("Age", min_value=0, value=0)
#     sex = st.selectbox("Sex", ["Male", "Female"])
#     chest_pain_type = st.number_input("Chest Pain Type", min_value=0, max_value=3, value=0, step=1)
#     resting_blood_pressure = st.number_input("Resting Blood Pressure", min_value=0, value=0)
#     serum_cholesterol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, value=0)
#     fasting_blood_sugar = st.number_input("Fasting Blood Sugar (> 120 mg/dl)", min_value=0, value=0)
#     max_heart_rate = st.number_input("Maximum Heart Rate", min_value=0, value=0)
#     exercise_induced_angina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
#     st_depression = st.number_input("ST Depression Induced by Exercise", min_value=0.0, value=0.0)
#     st_slope = st.number_input("Slope of the Peak Exercise ST Segment", min_value=0, max_value=2, value=0, step=1)
#     num_major_vessels = st.number_input("Number of Major Vessels Colored by Flourosopy", min_value=0, max_value=3, value=0, step=1)
#     thal = st.selectbox("Thal", ["Normal", "Fixed Defect", "Reversible Defect"])
#     return [age, sex, chest_pain_type, resting_blood_pressure, serum_cholesterol, fasting_blood_sugar, max_heart_rate, 
#             exercise_induced_angina, st_depression, st_slope, num_major_vessels, thal]


# def get_parkinsons_input():
#     st.subheader("Parkinson's Disease Prediction")
#     features = [
#         "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)",
#         "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)", "Shimmer:APQ3",
#         "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR", "RPDE", "DFA", "spread1", "spread2",
#         "D2", "PPE"
#     ]
#     inputs = []
#     for feature in features:
#         value = st.number_input(feature)
#         inputs.append(value)
#     return inputs

# # Main function to run the app
# def main():
#     st.sidebar.title("Multiple Disease Prediction System")
#     selected_option = st.sidebar.radio("Select Disease", ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"])

#     if selected_option == "Diabetes Prediction":
#         st.title('Diabetes Prediction using ML')
#         patient_name, mobile_number, gender = get_patient_info()
#         user_input = get_diabetes_input()
#         if st.button("Predict Diabetes"):
#             prediction = diabetes_model.predict([user_input])
#             if prediction[0] == 1:
#                 st.success("The person is diabetic")
#             else:
#                 st.success("The person is not diabetic")
#             # Check if patient exists in CSV
#             df = pd.read_csv("patient_info.csv")
#             idx = df[df['Name'] == patient_name].index
#             if len(idx) > 0:
#                 df.loc[idx, 'Diabetes Prediction'] = prediction[0]
#             else:
#                 new_row = {"Name": patient_name, "Mobile Number": mobile_number, "Gender": gender, 
#                            "Diabetes Prediction": prediction[0], "Heart Disease Prediction": np.nan, 
#                            "Parkinson's Prediction": np.nan}
#                 df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
#             df.to_csv("patient_info.csv", index=False)

#     elif selected_option == "Heart Disease Prediction":
#         st.title('Heart Disease Prediction using ML')
#         patient_name, mobile_number, gender = get_patient_info()
#         user_input = get_heart_disease_input()
#         if st.button("Predict Heart Disease"):
#             prediction = heart_disease_model.predict([user_input])
#             if prediction[0] == 1:
#                 st.success("The person is having heart disease")
#             else:
#                 st.success("The person does not have any heart disease")
#             # Check if patient exists in CSV
#             df = pd.read_csv("patient_info.csv")
#             idx = df[df['Name'] == patient_name].index
#             if len(idx) > 0:
#                 df.loc[idx, 'Heart Disease Prediction'] = prediction[0]
#             else:
#                 new_row = {"Name": patient_name, "Mobile Number": mobile_number, "Gender": gender, 
#                            "Diabetes Prediction": np.nan, "Heart Disease Prediction": prediction[0], 
#                            "Parkinson's Prediction": np.nan}
#                 df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
#             df.to_csv("patient_info.csv", index=False)

#     elif selected_option == "Parkinson's Prediction":
#         st.title("Parkinson's Disease Prediction using ML")
#         patient_name, mobile_number, gender = get_patient_info()
#         user_input = get_parkinsons_input()
#         if st.button("Predict Parkinson's Disease"):
#             prediction = parkinsons_model.predict([user_input])
#             if prediction[0] == 1:
#                 st.success("The person has Parkinson's disease")
#             else:
#                 st.success("The person does not have Parkinson's disease")
#             # Check if patient exists in CSV
#             df = pd.read_csv("patient_info.csv")
#             idx = df[df['Name'] == patient_name].index
#             if len(idx) > 0:
#                 df.loc[idx, "Parkinson's Prediction"] = prediction[0]
#             else:
#                 new_row = {"Name": patient_name, "Mobile Number": mobile_number, "Gender": gender, 
#                            "Diabetes Prediction": np.nan, "Heart Disease Prediction": np.nan, 
#                            "Parkinson's Prediction": prediction[0]}
#                 df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
#             df.to_csv("patient_info.csv", index=False)

# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

# loading the saved models
diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('saved_models/parkinsons_model.sav', 'rb'))

# Function to get user inputs for patient information
def get_patient_info():
    st.sidebar.subheader("Patient Information")
    name = st.sidebar.text_input("Name")
    mobile_number = st.sidebar.text_input("Mobile Number")
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    return name, mobile_number, gender

# Function to get user inputs for each disease prediction
def get_diabetes_input():
    st.subheader("Diabetes Prediction")
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=17, value=0, step=1)
    glucose = st.number_input("Glucose Level", min_value=0, value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, value=0)
    insulin = st.number_input("Insulin Level", min_value=0, value=0)
    bmi = st.number_input("BMI", min_value=0.0, value=0.0)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.0)
    age = st.number_input("Age", min_value=0, value=0)
    return [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]

def get_heart_disease_input():
    st.subheader("Heart Disease Prediction")
    age = st.number_input("Age", min_value=0, value=0)
    sex = st.selectbox("Sex", ["Male", "Female"])
    chest_pain_type = st.number_input("Chest Pain Type", min_value=0, max_value=3, value=0, step=1)
    resting_blood_pressure = st.number_input("Resting Blood Pressure", min_value=0, value=0)
    serum_cholesterol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, value=0)
    fasting_blood_sugar = st.number_input("Fasting Blood Sugar (> 120 mg/dl)", min_value=0, value=0)
    max_heart_rate = st.number_input("Maximum Heart Rate", min_value=0, value=0)
    exercise_induced_angina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
    st_depression = st.number_input("ST Depression Induced by Exercise", min_value=0.0, value=0.0)
    st_slope = st.number_input("Slope of the Peak Exercise ST Segment", min_value=0, max_value=2, value=0, step=1)
    num_major_vessels = st.number_input("Number of Major Vessels Colored by Flourosopy", min_value=0, max_value=3, value=0, step=1)
    thal = st.selectbox("Thal", ["Normal", "Fixed Defect", "Reversible Defect"])
    return [age, sex, chest_pain_type, resting_blood_pressure, serum_cholesterol, fasting_blood_sugar, max_heart_rate, 
            exercise_induced_angina, st_depression, st_slope, num_major_vessels, thal]

def get_parkinsons_input():
    st.subheader("Parkinson's Disease Prediction")
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
def view_patient_info():
    st.sidebar.subheader("View Patient Information")
    view_key = st.sidebar.text_input("Enter View Key", type="password")
    if view_key == "viewkey":
        show_data = st.sidebar.checkbox("Show Patient Data")
        if show_data:
            df = pd.read_csv("patient_info.csv")
            st.subheader("Patient Information")
            st.write(df)

# Main function to run the app
def main():
    st.sidebar.title("Multiple Disease Prediction System")
    view_patient_info()

    selected_option = st.sidebar.selectbox("Select Disease", ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"])

    if selected_option == "Diabetes Prediction":
        st.title('Diabetes Prediction using ML')
        patient_name, mobile_number, gender = get_patient_info()
        user_input = get_diabetes_input()
        if st.button("Predict Diabetes"):
            prediction = diabetes_model.predict([user_input])
            if prediction[0] == 1:
                st.success("The person is diabetic")
            else:
                st.success("The person is not diabetic")
            # Check if patient exists in CSV
            df = pd.read_csv("patient_info.csv")
            idx = df[df['Name'] == patient_name].index
            if len(idx) > 0:
                df.loc[idx, 'Diabetes Prediction'] = prediction[0]
                df.loc[idx, 'Timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                new_row = {"Name": patient_name, "Mobile Number": mobile_number, "Gender": gender, 
                           "Diabetes Prediction": prediction[0], "Heart Disease Prediction": np.nan, 
                           "Parkinson's Prediction": np.nan, "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv("patient_info.csv", index=False)

    elif selected_option == "Heart Disease Prediction":
        st.title('Heart Disease Prediction using ML')
        patient_name, mobile_number, gender = get_patient_info()
        user_input = get_heart_disease_input()
        if st.button("Predict Heart Disease"):
            prediction = heart_disease_model.predict([user_input])
            if prediction[0] == 1:
                st.success("The person is having heart disease")
            else:
                st.success("The person does not have any heart disease")
            # Check if patient exists in CSV
            df = pd.read_csv("patient_info.csv")
            idx = df[df['Name'] == patient_name].index
            if len(idx) > 0:
                df.loc[idx, 'Heart Disease Prediction'] = prediction[0]
                df.loc[idx, 'Timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                new_row = {"Name": patient_name, "Mobile Number": mobile_number, "Gender": gender, 
                           "Diabetes Prediction": np.nan, "Heart Disease Prediction": prediction[0], 
                           "Parkinson's Prediction": np.nan, "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv("patient_info.csv", index=False)

    elif selected_option == "Parkinson's Prediction":
        st.title("Parkinson's Disease Prediction using ML")
        patient_name, mobile_number, gender = get_patient_info()
        user_input = get_parkinsons_input()
        if st.button("Predict Parkinson's Disease"):
            prediction = parkinsons_model.predict([user_input])
            if prediction[0] == 1:
                st.success("The person has Parkinson's disease")
            else:
                st.success("The person does not have Parkinson's disease")
            # Check if patient exists in CSV
            df = pd.read_csv("patient_info.csv")
            idx = df[df['Name'] == patient_name].index
            if len(idx) > 0:
                df.loc[idx, "Parkinson's Prediction"] = prediction[0]
                df.loc[idx, 'Timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                new_row = {"Name": patient_name, "Mobile Number": mobile_number, "Gender": gender, 
                           "Diabetes Prediction": np.nan, "Heart Disease Prediction": np.nan, 
                           "Parkinson's Prediction": prediction[0], "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv("patient_info.csv", index=False)

if __name__ == "__main__":
    main()
