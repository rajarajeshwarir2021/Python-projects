import streamlit as st
from PIL import Image


st.subheader("Color to Grayscale Converter")
with st.expander("Start Camera"):
    # Start the camera
    org_img = st.camera_input("Camera")

    if org_img:
        # Create a pillow image instance
        img = Image.open(org_img)

        # Convert the pillow image to grayscale
        gray_img = img.convert("L")

        # Render the grayscale image on the webpage
        st.image(gray_img)