import pickle
import numpy as np
import streamlit as st

# Load the saved model
filename = 'Body_Metrics_final_model.pkl'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

# Custom CSS styling
st.markdown("""
    <style>
    .app-container {
        max-width: 600px;
        margin: auto;
        padding-top: 50px;
    }
    .app-title {
        text-align: center;
        font-size: 36px;
        color: #FF5733;
        font-family: 'Segoe UI', sans-serif;
    }
    .app-subtitle {
        text-align: center;
        font-size: 18px;
        color: #5D6D7E;
        margin-bottom: 30px;
    }
    .result {
        margin-top: 30px;
        background-color: #E8DAEF;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        color: #4A235A;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Begin centered container
st.markdown('<div class="app-container">', unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="app-title">🧍‍♂️ Weight Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">Enter your height (in feet) and get your predicted weight instantly</div>', unsafe_allow_html=True)

# Height input using slider for better UX
height_input = st.slider("Height (in feet):", min_value=3.0, max_value=7.5, value=5.8, step=0.1)

# Predict button
if st.button("🔍 Predict"):
    height_input_2d = np.array([[height_input]])
    predicted_weight = loaded_model.predict(height_input_2d)
    st.markdown(f'<div class="result">Predicted Weight: {predicted_weight[0, 0]:.2f} kg</div>', unsafe_allow_html=True)

# End container
st.markdown('</div>', unsafe_allow_html=True)
