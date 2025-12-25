import streamlit as st 
import pandas as pd
import joblib
import warnings
warnings.filterwarnings('ignore')

model =  joblib.load('knn_heart_model.pkl')
scaler = joblib.load("scaler.pkl")
expected_columns =  joblib.load("columns.pkl")



st.title('Cardio-Risk-ML-Model❤️')
st.markdown("This app predicts the risk of heart disease based on your input parameters.")

age = st.slider('Age', 18,100, 40)
sex= st.selectbox('Sex', ['Male', 'Female'])
chest_pain = st.selectbox('Chest Pain Type', ['ATA', 'TA', 'NAP', 'ASY'])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):

    # 1. Create raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak
    }

    # 2. Encode categorical features (match training exactly)
    raw_input['Sex_Male'] = 1 if sex == 'Male' else 0

    raw_input['ChestPainType_ATA'] = 1 if chest_pain == 'ATA' else 0
    raw_input['ChestPainType_NAP'] = 1 if chest_pain == 'NAP' else 0
    raw_input['ChestPainType_TA']  = 1 if chest_pain == 'TA' else 0

    raw_input['RestingECG_Normal'] = 1 if resting_ecg == 'Normal' else 0
    raw_input['RestingECG_ST']     = 1 if resting_ecg == 'ST' else 0

    raw_input['ExerciseAngina_Y'] = 1 if exercise_angina == 'Y' else 0

    raw_input['ST_Slope_Flat'] = 1 if st_slope == 'Flat' else 0
    raw_input['ST_Slope_Up']   = 1 if st_slope == 'Up' else 0

    # 3. Create DataFrame
    input_df = pd.DataFrame([raw_input])

    # 4. Add missing columns
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # 5. Reorder columns
    input_df = input_df[expected_columns]

    # 6. Scale input
    scaled_input = scaler.transform(input_df)

    # 7. Predict
    prediction = model.predict(scaled_input)[0]

    # 8. Show probability (if available)
    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(scaled_input)[0][1]
        st.metric("Heart Disease Risk Probability", f"{prob*100:.1f}%")

    # 9. Final output
    if prediction == 1:
        st.error("High Risk of Heart Disease")
    else:
        st.success("Low Risk of Heart Disease")
