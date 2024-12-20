# bot.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

print("Loading environment variables...")
load_dotenv()
print("Environment variables loaded.")

print("Configuring generative AI...")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
print("Generative AI configured.")

generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

print("Initializing the model...")
try:
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
        system_instruction=(
            "You are a history teacher called Indiana James and your job is to answer "
            "questions related to history. Describe the historic events didactically, "
            "using simple language and presenting the events by their dates as topics."
        ),
    )
    print("Model initialized successfully.")
except Exception as e:
    print(f"Error initializing model: {e}")

history = []

def get_response(user_input):
    try:
        print("Starting chat session...")
        chat_session = model.start_chat(history=history)
        print("Chat session started.")

        print("Sending user input to model...")
        response = chat_session.send_message(user_input)
        model_response = response.text
        print("Received response from model.")

        history.append({"role": "user", "parts": [user_input]})
        history.append({"role": "model", "parts": [model_response]})

        return model_response
    except Exception as e:
        print(f"Error in get_response: {e}")
        return "Sorry, something went wrong."