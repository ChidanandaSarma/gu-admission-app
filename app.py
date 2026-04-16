import streamlit as st
import pandas as pd
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

.custom-card {
    background: rgba(30, 41, 59, 0.8);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 0 25px rgba(168, 85, 247, 0.5);
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

body {
    background-color: #0f172a;
}

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

h1 {
    text-align: center;
    color: #e879f9;
}

.stButton>button {
    background: linear-gradient(90deg, #a855f7, #3b82f6);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #9333ea, #2563eb);
}

.stSelectbox, .stNumberInput {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1>🎓 Gauhati University Admission Predictor</h1>",
    unsafe_allow_html=True
)




data = pd.read_csv("cutoff.csv")


marks = st.number_input("Enter your marks (Best of 4)", 0.0, 100.0)

stream = st.selectbox("Select Stream", data["Stream"].unique())

category = st.selectbox("Select Category", data["Category"].unique())

courses = data[data["Stream"] == stream]["Course"].unique()
course = st.selectbox("Select Course", courses)

filtered = data[
    (data["Stream"] == stream) &
    (data["Category"] == category) &
    (data["Course"] == course)
]

st.markdown("""
<style>

/* Force dark theme */
html, body, [class*="css"]  {
    background-color: #0f172a !important;
    color: white !important;
}

/* Main app background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Labels */
label {
    color: white !important;
}

/* Inputs text */
input, select {
    color: white !important;
}

/* Fix dropdown */
div[data-baseweb="select"] {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)



if st.button("Check Admission Chance"):
    if len(filtered) > 0:
        cutoff = float(filtered["Cutoff"].values[0])

        if marks >= cutoff:
            st.success(f"✅ High chance! Cutoff was {cutoff}")
        elif marks >= cutoff - 5:
            st.warning(f"⚠️ Moderate chance! Cutoff was {cutoff}")
        else:
            st.error(f"❌ Low chance! Cutoff was {cutoff}")
    else:
        st.error("No data available")

st.markdown("---")

st.markdown(
    "<div style='text-align: center;'>"
    "Made by <b>Chidananda Sarma</b><br>"
    "Department of Computer Science<br>"
    "Gauhati University"
    "</div>",
    unsafe_allow_html=True
)
