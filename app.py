import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Wildlife Habitat Monitoring - Vietnam")

locations = {
    "Cat Ba Island": [20.72, 106.95, 20.85, 107.1],
    "Du Gia Nature Reserve": [22.6, 105.2, 23.0, 105.5],
    "Phong Nha-Ke Bang": [17.3, 105.8, 17.7, 106.3]
}

selected_location = st.selectbox("Select a Protected Area", list(locations.keys()))

# Fake time series data for now
years = np.arange(2017, 2025)
ndvi_values = np.random.uniform(0.4, 0.8, len(years))

st.subheader("NDVI Trend Over Time")
fig, ax = plt.subplots()
ax.plot(years, ndvi_values, marker='o')
ax.set_ylabel("NDVI")
ax.set_title(f"Vegetation Health in {selected_location}")
st.pyplot(fig)

