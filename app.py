import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(
    page_title="Rising Waters",
    page_icon="🌊",
    layout="centered"
)

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #0a1628;
    }
    .stApp {
        background: linear-gradient(135deg, #0a1628 0%, #1a3a5c 100%);
        color: white;
    }
    .title {
        text-align: center;
        font-size: 3em;
        color: #00d4ff;
        text-shadow: 0 0 20px #00d4ff;
        padding: 20px;
    }
    .subtitle {
        text-align: center;
        color: #7ec8e3;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .result-box {
        background: rgba(0, 212, 255, 0.1);
        border: 2px solid #00d4ff;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
    }
    .stSlider > div > div {
        background-color: #00d4ff;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open('water_model.pkl', 'rb'))

# Title
st.markdown('<p class="title">🌊 Rising Waters</p>', 
            unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-Powered Flood Prediction System</p>', 
            unsafe_allow_html=True)

st.markdown("---")

# Two columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌡️ Temperature")
    temperature = st.slider("Temperature (°C)", 
                           15.0, 35.0, 25.0)

with col2:
    st.markdown("### 🌧️ Precipitation")
    precipitation = st.slider("Precipitation (mm)", 
                             100, 200, 150)

st.markdown("---")

# Big predict button
if st.button("🔮 PREDICT WATER LEVEL", 
             use_container_width=True):
    result = model.predict([[temperature, precipitation]])
    level = result[0]
    
    st.markdown('<div class="result-box">', 
                unsafe_allow_html=True)
    st.markdown(f"## 💧 Water Level: {level:.2f} meters")
    
    if level > 3.9:
        st.error("🚨 DANGER! Very High Flood Risk!")
        st.progress(100)
    elif level > 3.6:
        st.warning("⚠️ WARNING! Rising Water Levels!")
        st.progress(70)
    else:
        st.success("✅ SAFE! Normal Water Level")
        st.progress(30)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<center>🌊 Rising Waters Project | "
    "Built with Python & Streamlit</center>",
    unsafe_allow_html=True
)