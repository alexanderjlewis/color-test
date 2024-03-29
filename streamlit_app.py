import streamlit as st
from PIL import Image
import cv2
from colorblind import colorblind

st.title("Colour Blindness Simulator")

uploaded_img = st.file_uploader("Upload Image")

if uploaded_img is not None:
    st.title("Original Image")
    img = Image.open(uploaded_img)
    img = Image.convert('RGB')
    st.image(img, "")

    
    
    st.title("Simulated Images")
    # simulate protanopia
    simulated_img = colorblind.simulate_colorblindness(img, colorblind_type='protanopia')

    st.image(simulated_img, "Simulated Protanopia")

    # simulate tritanopia
    simulated_img = colorblind.simulate_colorblindness(img, colorblind_type='tritanopia')

    st.image(simulated_img, "Simulated Tritanopia")

    # simulate deuteranopia
    simulated_img = colorblind.simulate_colorblindness(img, colorblind_type='deuteranopia')

    st.image(simulated_img, "Simulated Deuteranopia")
