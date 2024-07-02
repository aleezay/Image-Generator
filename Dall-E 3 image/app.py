#import neccessary modules
from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey



st.set_page_config(page_title="Dalle-Image-Generation", page_icon=":camera", layout="wide")

#create a title

st.title("Dall-E-3 Image Generation Tool")

#create a subheader

st.subheader("Powered by the world's most powerful image generation API - Dall-e")
img_description = st.text_input("enter description for image you want to generate")
num_of_images = st.number_input("Select the number of images you want to generate", min_value=1, max_value=10, value=1)

#creat a button
if st.button("Generate Images"):
    pass