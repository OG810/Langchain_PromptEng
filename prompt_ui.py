from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
import os 
# Get the key from the environment


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
model=ChatGoogleGenerativeAI(model='models/gemini-2.5-flash', google_api_key=api_key)

st.header("Research tool")
user_input=st.text_input("Enter your prompt")

if st.button("Summarize"):
    result=model.invoke(user_input)
    st.write(result.content)
