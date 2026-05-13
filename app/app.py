import streamlit as st
import pandas as pd
import joblib
import os

# LOAD FILES


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(
    os.path.join(BASE_DIR, "..", "src", "model.pkl")
)

scaler = joblib.load(
    os.path.join(BASE_DIR, "..", "src", "scaler.pkl")
)

columns = joblib.load(
    os.path.join(BASE_DIR, "..", "src", "columns.pkl")
)
# PAGE CONFIG

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

# TITLE

st.title("📊 Customer Churn Prediction System")

st.markdown(
    """
Predict whether a telecom customer is likely to churn using Machine Learning.
"""
)

st.divider()


# USER INPUTS


st.subheader("📌 Customer Information")

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

SeniorCitizen = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

Partner = st.selectbox(
    "Has Partner?",
    ["Yes", "No"]
)

Dependents = st.selectbox(
    "Has Dependents?",
    ["Yes", "No"]
)

tenure = st.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

PhoneService = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

MultipleLines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

InternetService = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

OnlineSecurity = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

OnlineBackup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

DeviceProtection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

TechSupport = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

StreamingTV = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

StreamingMovies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

Contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

PaperlessBilling = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.slider(
    "Monthly Charges",
    0.0,
    200.0,
    70.0
)

TotalCharges = st.slider(
    "Total Charges",
    0.0,
    10000.0,
    2500.0
)

# CREATE INPUT DATAFRAME


input_dict = {
    "SeniorCitizen": SeniorCitizen,
    "tenure": tenure,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}

input_df = pd.DataFrame(
    columns=columns
)

input_df.loc[0] = 0

# Add numeric values
for key, value in input_dict.items():
    if key in input_df.columns:
        input_df[key] = value


# HANDLE CATEGORICAL FEATURES

categorical_inputs = {
    "gender": gender,
    "Partner": Partner,
    "Dependents": Dependents,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod
}

for feature, value in categorical_inputs.items():

    column_name = f"{feature}_{value}"

    if column_name in input_df.columns:
        input_df[column_name] = 1

# SCALE INPUT

input_scaled = scaler.transform(input_df)

# PREDICTION

if st.button("🔍 Predict Churn"):

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(
        input_scaled
    )[0][1]

    st.divider()

    st.subheader("📈 Prediction Result")

    if prediction == 1:

        st.error(
            f"⚠️ Customer is likely to churn."
        )

    else:

        st.success(
            f"✅ Customer is likely to stay."
        )

    st.metric(
        "Churn Probability",
        f"{probability * 100:.2f}%"
    )

    st.divider()

    # ==============================
    # BUSINESS INSIGHTS
    # ==============================

    st.subheader("🧠 Business Insights")

    if probability > 0.7:

        st.warning(
            """
High-risk customer detected.

Recommended actions:
- Offer discount plans
- Improve support
- Provide loyalty benefits
"""
        )

    elif probability > 0.4:

        st.info(
            """
Moderate churn risk.

Recommended actions:
- Monitor customer satisfaction
- Offer personalized engagement
"""
        )

    else:

        st.success(
            """
Low churn risk customer.

Customer is likely satisfied with services.
"""
        )

# FOOTER

st.divider()

st.caption(
    "Built with ❤️ using Machine Learning & Streamlit"
)