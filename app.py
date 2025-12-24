import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("credit_approval_rfmodel.pkl")

st.title("Credit Card Approval Prediction")

st.write(
    "This model predicts credit card approval while prioritizing precision "
    "to minimize risky approvals."
)

# ---- User Inputs (MATCH training features exactly) ----
gender = st.radio("Applicant Gender", ["Male", "Female"])
gender_encoded = 1 if gender == "Male" else 0
income = st.number_input("Total_Income", min_value=0)
good_debt = st.number_input("Total_Good_Debt", min_value=0)
bad_debt = st.number_input("Total_Bad_Debt", min_value=0)
credit_score = good_debt-bad_debt

# Convert to DataFrame
input_df = pd.DataFrame([{
    "gender": gender,
    "income": income,
    "good_debt": good_debt,
    "bad_debt": bad_debt,
    "credit_score": credit_score
}])

# ---- Prediction ----
threshold = st.slider(
    "Approval Threshold (higher = stricter)",
    min_value=0.0,
    max_value=1.0,
    value=0.7
)

if st.button("Predict"):
    prob = model.predict_proba(input_df)[0][1]

    if prob >= threshold:
        st.success(f"Approved | Approval Probability: {prob:.2f}")
    else:
        st.error(f"Rejected | Risk Probability: {1 - prob:.2f}")