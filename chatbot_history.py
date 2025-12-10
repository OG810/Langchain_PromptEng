## this will contain the code for chatbot based communication 
## but this chatbot will have the stored chats history in list  


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv() ## loading the environemnt varibles
api_key = os.getenv("GOOGLE_API_KEY") ## creating the varibles for api key 
model=ChatGoogleGenerativeAI(model='models/gemini-2.5-flash', google_api_key=api_key) ## loading the model

chat_history=[]
## list is created which will store the previous conversationof the suer and AI and everytime and this list of chat hostories 
##will also be passed to the ai model thru api thru invoke method


while True:
    user_input=input('You: ')
    chat_history.append(user_input)
    if user_input=='exit':
        break
    result=model.invoke(chat_history) 
    chat_history.append(result)

    print('AI: ', result.content) 
print(chat_history)    
## now we get here only list which has all messages but we dont know which message is exactly sent by user and which one by ai 
## we try to implement the dictionary of chat_history={}where we store {you:"dfdfdf"."efdfd","fs..df",AI:"hgdhgsh","sjdgjag","./.hds"}

## but to this also langchain alsreday solved this problem by creating 3 inbuilt functions of SystemMessages, HumanMessages, AIMessages
## we can use them directly 
## this is used in new code file 