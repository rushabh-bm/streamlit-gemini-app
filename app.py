from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

import streamlit as st 
import os
import google.generativeai as genai 


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Create a new instance of the client

# FUNCTION TO LOAD GEMINI PRO MODEL AND GET RESPONSE
model = genai.GenerativeModel("gemini-1.5-pro-latest")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#initializing our streamlit app
st.set_page_config(page_title="Q&A demo ")

st.header("RUSHABH LLM Application")

input=st.text_input("Input: ",key ="input")
submit = st.button("Ask the Question")

# when the submit is clicked 
if submit:
    response = get_gemini_response(input)
    st.write("Response: ", response)
