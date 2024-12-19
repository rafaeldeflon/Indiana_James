import os
import google.generativeai as genai
from dotenv import load_dotenv

print("Loading environment variables...")
# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key for GEMINI_API_KEY not found in environment variables.")

print("Configuring generative AI...")
genai.configure(api_key=api_key)

# Create the model
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

try:
    print("Initializing the model...")
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
        system_instruction=(
            "You are a history teacher called Indiana James and your job is to answer questions related to history. "
            "Describe the historic events didactically, using simple language and presenting the events by their dates as topics."
        ),
    )

    history = []

    print("Bot: Hello, my name is Indiana James, lets learn some history today?")

    while True:
        user_input = input("You: ")
        print("User input received:", user_input)

        chat_session = model.start_chat(
            history=history
        )
        print("Chat session started...")

        response = chat_session.send_message(user_input)
        print("Response received from the model...")

        model_response = response.text
        print(f"Bot: {model_response}")
        print()

        history.append({"role": "user", "parts": [user_input]})
        history.append({"role": "model", "parts": [model_response]})

except Exception as e:
    print(f"An error occurred: {e}")