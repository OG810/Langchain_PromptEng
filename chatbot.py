## this will contain the code for chatbot based communication 
## but this chatbot will not have the memeory for the past chats 


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv() ## loading the environemnt varibles
api_key = os.getenv("GOOGLE_API_KEY") ## creating the varibles for api key 
model=ChatGoogleGenerativeAI(model='models/gemini-2.5-flash', google_api_key=api_key) ## loading the model

while True:
    user_input=input('You: ')
    if user_input=='exit':
        break
    result=model.invoke(user_input) 
    print('AI: ', result.content)   




