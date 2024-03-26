import altair as alt
import base64
import os
from typing import Dict
import requests
import pandas as pd
import streamlit as st
from io import BytesIO
from PIL import Image
from typing import List, Dict

import numpy as np
import cv2
from colorblind import colorblind
import matplotlib.pyplot as plt

st.title("Colour Bling Simulator")

uploaded_img = st.file_uploader("Upload Image")

if uploaded_img is not None:
    img = Image.open(uploaded_img)
    
    st.image(img, "Uploaded image")
    
    # simulate protanopia
    simulated_img = colorblind.simulate_colorblindness(img, colorblind_type='protanopia')

    st.image(simulated_img, "Uploaded image")
