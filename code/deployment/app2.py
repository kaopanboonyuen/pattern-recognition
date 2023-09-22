import streamlit as st
import tensorflow as tf
import random
from PIL import Image, ImageOps
import numpy as np

import warnings
warnings.filterwarnings("ignore")

with st.sidebar:
        st.image('mg.png')
        st.title("Mangifera Healthika")
        st.subheader("Accurate detection of diseases present in the mango leaves. This helps an user to easily detect the disease and identify it's cause.")         
        

st.write("""
         # Mango Disease Detection with Remedy Suggestion
         """
         )