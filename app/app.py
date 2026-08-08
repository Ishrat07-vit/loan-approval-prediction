import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/loan_model.pkl")

st.title("🏦 Loan Approval Prediction")
st.write("Enter the applicant details below:")

# Input features

no_of_dependents = st.number_input(
    "Number of Dependents",
    min_value=0,
    max_value=10,
    value=0
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

income_annum = st.number_input(
    "Annual Income",
    min_value=0,
    value=0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    value=0
)

loan_term = st.number_input(
    "Loan Term (Months)",
    min_value=1,
    value=1
)

cibil_score = st.number_input(
    "CIBIL Score",
    min_value=300,
    max_value=900,
    value=700
)

residential_assets_value = st.number_input(
    "Residential Assets Value",
    min_value=0,
    value=0
)

commercial_assets_value = st.number_input(
    "Commercial Assets Value",
    min_value=0,
    value=0
)

luxury_assets_value = st.number_input(
    "Luxury Assets Value",
    min_value=0,
    value=0
)

bank_asset_value = st.number_input(
    "Bank Asset Value",
    min_value=0,
    value=0
)

# Encode categorical values

education_encoded = 1 if education == "Graduate" else 0
self_employed_encoded = 1 if self_employed == "Yes" else 0

# Prediction

if st.button("Predict"):

    data = pd.DataFrame({
        "no_of_dependents": [no_of_dependents],
        "education": [education_encoded],
        "self_employed": [self_employed_encoded],
        "income_annum": [income_annum],
        "loan_amount": [loan_amount],
        "loan_term": [loan_term],
        "cibil_score": [cibil_score],
        "residential_assets_value": [residential_assets_value],
        "commercial_assets_value": [commercial_assets_value],
        "luxury_assets_value": [luxury_assets_value],
        "bank_asset_value": [bank_asset_value]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")