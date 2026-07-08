import streamlit as st
import pickle
import numpy as np

# ===========================
# Page Configuration
# ===========================

st.set_page_config(
    page_title="Salary Prediction",
    page_icon="💰",
    layout="centered"
)

# ===========================
# Load Model
# ===========================

with open("linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

# ===========================
# Title
# ===========================

st.title("💰 Employee Salary Prediction")

st.write(
    """
    This Machine Learning application predicts an employee's salary
    based on the number of years of experience using **Linear Regression**.
    """
)

st.divider()

# ===========================
# User Input
# ===========================

experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=1.0,
    step=0.5
)

# ===========================
# Prediction
# ===========================

if st.button("Predict Salary"):

    prediction = model.predict(np.array([[experience]]))

    st.success(
        f"Predicted Salary: ₹ {prediction[0]:,.2f}"
    )

# ===========================
# Sidebar
# ===========================

st.sidebar.header("About")

st.sidebar.write(
"""
Model : Linear Regression

Algorithm : Supervised Machine Learning

Feature :
- Years of Experience

Target :
- Salary
"""
)

# ===========================
# Footer
# ===========================

st.markdown("---")

st.caption("Developed using Streamlit and Scikit-Learn")