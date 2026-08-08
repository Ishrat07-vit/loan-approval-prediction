# 🏦 Loan Approval Prediction

An end-to-end Machine Learning project that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant financial and personal information.

The project includes data preprocessing, exploratory data analysis, model training, model evaluation, model serialization using Joblib, and an interactive Streamlit web application.

---

## 🚀 Live Demo

Try the deployed application:

👉 **[Loan Approval Prediction App](https://loan-approval-prediction-07.streamlit.app/)**

The application allows users to enter applicant details and receive a real-time loan approval prediction using the trained Machine Learning model.

---

## 📌 Problem Statement

Loan approval decisions depend on several factors such as income, credit score, loan amount, employment status, assets, and number of dependents.

This project uses Machine Learning to learn patterns from historical loan application data and predict the loan approval status for a new applicant.

---

## 🎯 Objectives

- Perform exploratory data analysis on loan application data
- Preprocess numerical and categorical features
- Train a Logistic Regression classification model
- Evaluate the trained model
- Save the trained model using Joblib
- Build an interactive Streamlit application
- Provide real-time loan approval predictions

---

## 📊 Features Used

The model uses the following 11 features:

| Feature | Description |
|---|---|
| `no_of_dependents` | Number of dependents |
| `education` | Education status |
| `self_employed` | Self-employment status |
| `income_annum` | Annual income |
| `loan_amount` | Requested loan amount |
| `loan_term` | Loan term in months |
| `cibil_score` | Applicant's CIBIL credit score |
| `residential_assets_value` | Value of residential assets |
| `commercial_assets_value` | Value of commercial assets |
| `luxury_assets_value` | Value of luxury assets |
| `bank_asset_value` | Value of bank assets |

### Target

```text
loan_status