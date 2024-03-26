import streamlit as st
from PIL import Image
from colorblind import colorblind

st.title("Colour Bling Simulator")

uploaded_img = st.file_uploader("Upload Image")

if uploaded_img is not None:
    img = Image.open(uploaded_img)
    
    st.image(img, "Uploaded image")
    
    # simulate protanopia
    simulated_img = colorblind.simulate_colorblindness(img, colorblind_type='protanopia')

    st.image(simulated_img, "Uploaded image")
