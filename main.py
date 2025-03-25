import streamlit as st
import numpy as np
import pickle
import os

os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

# Load the models for fertilizer prediction
classifier_model = pickle.load(open('classifier.pkl', 'rb'))
label_encoder = pickle.load(open('fertilizer.pkl', 'rb'))

# Sidebar
st.sidebar.title("FarmAura")
app_mode = st.sidebar.selectbox("Select page from the dropdown menu", ["Home", "Fertilizer Prediction"])

# Mapping for soil and crop types
soil_mapping = {
    "Black": 0,
    "Clayey": 1,
    "Loamy": 2,
    "Red": 3,
    "Sandy": 4
}

crop_mapping = {
    "Barley": 0,
    "Cotton": 1,
    "Ground Nuts": 2,
    "Maize": 3,
    "Millets": 4,
    "Oil Seeds": 5,
    "Paddy": 6,
    "Pulses": 7,
    "Sugarcane": 8,
    "Tobacco": 9,
    "Wheat": 10
}

# Main Page
if app_mode == "Home":
    st.header("FERTILIZER PREDICTION SYSTEM")
    image_path = "home.jpeg"
    st.image(image_path, use_container_width=True)
    st.markdown("""
    # 🌿 Welcome to the Crop's Fertilizer Prediction System! 🔍

Identify the required Crop's Fertilizer effortlessly with our advanced prediction system. Upload the values, and let our technology do the rest.

---

## 🚀 Get Started
1. **Upload Your data**: Navigate to the **Crop's Fertilizer Prediction Page**.
2. **Instant Analysis**: Our system processes your image with state-of-the-art algorithms.
3. **Receive Results**: Get immediate feedback and recommendations.

---

## 📋 Steps to Use
1. **Visit the Crop's Fertilizer Prediction Page**
2. **Upload the required values regarding your crop**
3. **Wait for the System to Analyze**
4. **View Results and Recommendations**
                """)

# Fertilizer Prediction Page[GitHub](https://github.com)
elif app_mode == "Fertilizer Prediction":
    st.header("Fertilizer Prediction")
    temp = st.slider("Temperature", min_value=0, max_value=100, step=1)
    humi = st.slider("Humidity", min_value=0, max_value=100, step=1)
    mois = st.slider("Moisture", min_value=0, max_value=100, step=1)
    soil = st.selectbox("Soil Type", ["Black", "Clayey", "Loamy", "Red", "Sandy"])
    crop = st.selectbox("Crop Type", ["Barley", "Cotton", "Ground Nuts", "Maize", "Millets", "Oil Seeds", "Paddy", "Pulses", "Sugarcane", "Tobacco", "Wheat"])
    nitro = st.slider("Nitrogen", min_value=0, max_value=100, step=1)
    pota = st.slider("Potassium", min_value=0, max_value=100, step=1)
    phosp = st.slider("Phosphorus", min_value=0, max_value=100, step=1)

    # Convert categorical inputs to numerical values
    soil_encoded = soil_mapping[soil]
    crop_encoded = crop_mapping[crop]

    # Predict button
    if st.button("Predict"):
        input_data = [int(temp), int(humi), int(mois), soil_encoded, crop_encoded, int(nitro), int(pota), int(phosp)]
        input_array = np.array(input_data).reshape(1, -1)
        result_index = classifier_model.predict(input_array)
        result_label = label_encoder.inverse_transform(result_index)
        st.success(f'Predicted Fertilizer is {result_label[0]}')
