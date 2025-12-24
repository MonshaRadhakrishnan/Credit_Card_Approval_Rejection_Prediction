import streamlit as st
import base64
import pandas as pd
import joblib

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Credit Card Approval Prediction",
    layout="centered"
)

# --------------------------------------------------
# Background Image (FAIL-SAFE)
# --------------------------------------------------
def set_bg_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()

        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("Background image not found. Running without background.")

set_bg_image("credit_card_check.png")

# --------------------------------------------------
# Global CSS (overlay + button + alerts)
# --------------------------------------------------
st.markdown(
    """
    <style>
    .block-container {
        background-color: rgba(0, 0, 0, 0.55);
        padding: 2rem;
        border-radius: 12px;
    }

    h1, h2, h3, label, p {
        color: white !important;
    }

    div.stButton > button {
        background-color: #1f77b4;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #155a8a;
        color: white;
    }

    .stAlert.success {
        background-color: rgba(40, 167, 69, 0.95);
        color: white;
        font-weight: 600;
        border-radius: 10px;
    }

    .stAlert.error {
        background-color: rgba(220, 53, 69, 0.95);
        color: white;
        font-weight: 600;
        border-radius: 10px;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Load trained model
# --------------------------------------------------
model = joblib.load("credit_approval_rfmodel.pkl")

# --------------------------------------------------
# App UI
# --------------------------------------------------
st.title("Credit Card Approval Prediction")

st.write(
        "Fill in the applicant details below to evaluate eligibility"
        "The total credit score, derived from good and bad debt history, helps indicate approval likelihood."
)

st.markdown("---")
# ---- User Inputs (MATCH training features exactly) ----
gender = st.radio("Applicant_Gender", ["Male", "Female"])
gender_encoded = 1 if gender == "Male" else 0
age = st.number_input("Applicant_Age",min_value=18)
income = st.number_input("Total_Income", min_value=0)
good_debt = st.number_input("Total_Good_Debt", min_value=0)
bad_debt = st.number_input("Total_Bad_Debt", min_value=0)
credit_score = good_debt-bad_debt

# Convert to DataFrame
input_df = pd.DataFrame(
    [[
        gender_encoded,
        age,
        income,
        bad_debt,
        good_debt,
        credit_score
    ]],
    columns=[
        "Applicant_Gender",
        "Applicant_Age",
        "Total_Income",
        "Total_Bad_Debt",
        "Total_Good_Debt",
        "Total_Credit_Score"
    ]
)
st.markdown("---")

# --------------------------------------------------
# Prediction (FIXED THRESHOLD)
# --------------------------------------------------
FIXED_THRESHOLD = 0.7  # Business-defined decision rule


if st.button("Predict"):
    prob = model.predict_proba(input_df)[0][1]

    if prob >= FIXED_THRESHOLD:
        st.success(f" APPROVED\n\nApproval Probability: {prob:.2f} \n\nYour Total Credit Score is: {credit_score}")
    else:
        st.error(f" REJECTED\n\nRisk Probability: {1 - prob:.2f} \n\nYour Total Credit Score is: {credit_score}")

st.markdown(
    """
    <hr>
    <p style='font-size: 13px; color: #cccccc; text-align: center;'>
        This application is built using a synthetic dataset for demonstration and learning purposes.
        It does not represent real customer data or real-world credit decisioning systems.
    </p>
    """,
    unsafe_allow_html=True
)
