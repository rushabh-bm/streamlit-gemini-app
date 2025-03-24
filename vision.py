from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

import streamlit as st 
import os
import google.generativeai as genai 
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# FUNCTION TO LOAD GEMINI PRO MODEL AND GET RESPONSE
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else: 
        response=model.generate_content(image)
    return response.text


st.set_page_config(page_title="Iamge  Demo ")

st.header("RUSHABH's LLM Application")


# File uploader for image input
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

# Text input for user query
user_prompt = st.text_area("Enter your question about the image:")

if st.button("Tell me About the Image"):
    if uploaded_file and user_prompt:
        # Open the image
        image = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Send image & text to Gemini
        response = model.generate_content([user_prompt, image])

        # Display response
        st.subheader("AI Response:")
        st.write(response.text)
    else:
        st.warning("Please upload an image and enter a question!")

