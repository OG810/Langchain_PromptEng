from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv() ## loading the environemnt varibles
api_key = os.getenv("GOOGLE_API_KEY") ## creating the varibles for api key 
model=ChatGoogleGenerativeAI(model='models/gemini-2.5-flash', google_api_key=api_key) ## loading the model


messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)