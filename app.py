import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("best_churn_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("📊 Telco Customer Churn Prediction App")
st.write("Enter customer details below to predict churn probability.")

# Inputs (same order as X.columns)
def user_input_features():
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    tenure = st.number_input("Tenure (Months)", 0, 100, 12)
    MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.35)
    TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 500.0)

    Female = st.selectbox("Gender (Female=1, Male=0)", [0, 1])
    Partner_Yes = st.selectbox("Partner", [0, 1])
    Dependents_Yes = st.selectbox("Dependents", [0, 1])
    PhoneService_Yes = st.selectbox("Phone Service", [0, 1])

    MultipleLines_Yes = st.selectbox("Multiple Lines Yes", [0, 1])

    InternetService_Fiber_optic = st.selectbox("Fiber Optic Internet", [0, 1])
    InternetService_No = 0  # reference dropped

    OnlineSecurity_Yes = st.selectbox("Online Security Yes", [0, 1])
    OnlineBackup_Yes = st.selectbox("Online Backup Yes", [0, 1])
    DeviceProtection_Yes = st.selectbox("Device Protection Yes", [0, 1])
    TechSupport_Yes = st.selectbox("Tech Support Yes", [0, 1])
    StreamingTV_Yes = st.selectbox("Streaming TV Yes", [0, 1])
    StreamingMovies_Yes = st.selectbox("Streaming Movies Yes", [0, 1])

    Contract_One_year = st.selectbox("Contract One Year", [0, 1])
    Contract_Two_year = st.selectbox("Contract Two Year", [0, 1])

    PaperlessBilling_Yes = st.selectbox("Paperless Billing Yes", [0, 1])

    PaymentMethod_Electronic_check = st.selectbox("Electronic Check", [0, 1])
    PaymentMethod_Mailed_check = st.selectbox("Mailed Check", [0, 1])
    PaymentMethod_Credit_card_automatic = 0  # reference dropped

    data = {
        'SeniorCitizen': SeniorCitizen,
        'tenure': tenure,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges,
        'Female': Female,
        'Partner_Yes': Partner_Yes,
        'Dependents_Yes': Dependents_Yes,
        'PhoneService_Yes': PhoneService_Yes,
        'MultipleLines_Yes': MultipleLines_Yes,
        'InternetService_Fiber optic': InternetService_Fiber_optic,
        'OnlineSecurity_Yes': OnlineSecurity_Yes,
        'OnlineBackup_Yes': OnlineBackup_Yes,
        'DeviceProtection_Yes': DeviceProtection_Yes,
        'TechSupport_Yes': TechSupport_Yes,
        'StreamingTV_Yes': StreamingTV_Yes,
        'StreamingMovies_Yes': StreamingMovies_Yes,
        'Contract_One year': Contract_One_year,
        'Contract_Two year': Contract_Two_year,
        'PaperlessBilling_Yes': PaperlessBilling_Yes,
        'PaymentMethod_Electronic check': PaymentMethod_Electronic_check,
        'PaymentMethod_Mailed check': PaymentMethod_Mailed_check
    }

    return pd.DataFrame([data])

# Get user input
input_df = user_input_features()

# Scale
scaled_input = scaler.transform(input_df)

# Predict
prediction = model.predict(scaled_input)[0]
prob = model.predict_proba(scaled_input)[0][1]

st.subheader("🔍 Prediction:")
if prediction == 1:
    st.error("❌ The customer is likely to CHURN")
else:
    st.success("✅ The customer is NOT likely to churn")

st.subheader("📈 Churn Probability:")
st.write(f"**{prob:.2f}**")
