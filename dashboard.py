import streamlit as st
import pandas as pd
import pickle
import numpy as np
import plotly.express as px

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.report_generator import generate_report

# Load model + data
model = pickle.load(open("models/performance_model.pkl", "rb"))
df = pd.read_csv("data/raw/employees.csv")

st.set_page_config(page_title="HR Analytics System", layout="wide")

st.title("🏢 Employee Performance Predictor")

# ---------------- INPUTS (MATCH MODEL EXACTLY) ----------------
age = st.sidebar.slider("Age", 20, 60, 30)
experience = st.sidebar.slider("Experience", 0, 40, 5)
salary = st.sidebar.slider("Salary", 20000, 150000, 50000)
training = st.sidebar.slider("Training Hours", 0, 100, 40)
attendance = st.sidebar.slider("Attendance %", 0, 100, 80)

employee = [age, experience, salary, training, attendance]

# ---------------- PREDICTION ----------------
if st.button("Predict Performance"):

    pred = model.predict([employee])[0]

    if pred == 0:
        st.error("🔴 Low Performer")
        label = "Low Performer"
    elif pred == 1:
        st.warning("🟡 Medium Performer")
        label = "Medium Performer"
    else:
        st.success("🟢 High Performer")
        label = "High Performer"

# ---------------- PDF REPORT ----------------
if st.button("Generate HR Report"):

    pred = model.predict([employee])[0]

    if pred == 0:
        label = "Low Performer"
    elif pred == 1:
        label = "Medium Performer"
    else:
        label = "High Performer"

    generate_report(employee, label)

    st.success("📄 HR Report Generated!")

# ---------------- DASHBOARD ----------------
st.subheader("HR Analytics")

col1, col2, col3 = st.columns(3)

col1.metric("Employees", len(df))
col2.metric("Avg Salary", round(df["salary"].mean(), 2))
col3.metric("Avg Experience", round(df["experience"].mean(), 2))

fig = px.histogram(df, x="performance", color="performance")
st.plotly_chart(fig, use_container_width=True)

fig2 = px.scatter(df, x="experience", y="salary", color="performance")
st.plotly_chart(fig2, use_container_width=True)