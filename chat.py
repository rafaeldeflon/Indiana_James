import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="You are a history teacher called Indiana James and your job is to answer questions related to history. Describe the historic events didactically, using simple language and presenting the events by their dates as topics.",
)

history = []

print("Bot: Hello, my name is Indiana James, lets learn some history today?")

while True:
    user_input = input("You: ")

    chat_session = model.start_chat(
        history=history
    )

    response = chat_session.send_message(user_input)

    model_response = response.text
    print(f"Bot: {model_response}")
    print()

    history.append({"role": "user", "parts":[user_input]})
    history.append({"role": "model", "parts":[model_response]})
