"""
## Test 1 : to check the list of API callable models from google gemini
## we have added this segment of test 1 to see the required models that can be caaled using api of google ai studio

from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# List available models
models = genai.list_models()

for m in models:
    print(m.name, " | supports: ", m.supported_generation_methods)
"""