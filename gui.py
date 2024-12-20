# main.py

import tkinter as tk
from tkinter import scrolledtext
import threading
from bot import get_response

# Function to handle sending messages
def send_message(event=None):
    user_input = user_entry.get()
    if user_input.strip() == "":
        return

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You: {user_input}\n")
    chat_box.config(state=tk.DISABLED)

    # Clear the user input field
    user_entry.delete(0, tk.END)

    # Get response from the chat bot
    def get_and_display_response():
        model_response = get_response(user_input)
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f"Bot: {model_response}\n\n")
        chat_box.config(state=tk.DISABLED)
        chat_box.yview(tk.END)

    threading.Thread(target=get_and_display_response).start()

# Set up the main application window
print("Setting up the main application window...")
root = tk.Tk()
print("Main application window set up.")

root.title("Indiana James - History Chatbot")

# Customize the window size
root.geometry("500x600")

# Create a scrolled text widget for the chat box
print("Creating chat box...")
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
print("Chat box created.")

# Create an entry widget for user input
print("Creating user entry...")
user_entry = tk.Entry(root, width=80)
user_entry.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X, expand=True)
user_entry.bind("<Return>", send_message)  # Bind the Enter key to send messages
print("User entry created.")

# Create a button to send messages
print("Creating send button...")
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)
print("Send button created.")

# Start the chat with a greeting
def start_chat():
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Bot: Hello, my name is Indiana James, let's learn some history today?\n\n")
    chat_box.config(state=tk.DISABLED)
    print("Chat started")

print("Starting chat...")
start_chat()

# Run the main application loop
print("Running main loop...")
root.mainloop()
print("Main loop is running")