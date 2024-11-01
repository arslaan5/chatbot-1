import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
import streamlit as st

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


# Function to get the response
def get_response(request):
    llm = GoogleGenerativeAI(api_key=api_key,
    model="gemini-1.5-flash",
    temperature=0.3
    )
    if not request:
        return "Please enter a prompt"
    response = llm.invoke(request)
    return response

# Initialize the streamlit app
st.set_page_config(page_title="AI Chatbot")
st.title("Get your queries solved!")
st.header("A simple chatbot by Arslaan")

input_field = st.text_input("Enter your query", key="input_field", placeholder="Type here")

submit_btn = st.button("Get response")

response = get_response(input_field)

if submit_btn:
    st.subheader("Generated response:")
    st.write(response)