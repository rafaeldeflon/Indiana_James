# Configuration for the GUI of the chatbot

# Importing necessary libraries

import tkinter as tk
from tkinter import scrolledtext    # Tkinter to build the chat GUI
from PIL import Image, ImageTk      # PIL for image handling
import threading
from bot import get_response        # Importing the bot from bot.py
import os

# Configuration of the chatbox in the GUI

    # Function to handle sending messages
def send_message(event=None):
    user_input = user_entry.get()
    if user_input.strip() == "":
        return

    # Display user message with image
    display_message(user_input, "user")

    # Clear the user input field
    user_entry.delete(0, tk.END)

    # Get response from the chat bot (calling the function from bot.py)
    def get_and_display_response():
        model_response = get_response(user_input)
        display_message(model_response, "bot")

    threading.Thread(target=get_and_display_response).start()

def display_message(message, sender):
    chat_box.config(state=tk.NORMAL)

    # Create a frame to hold image and text
    msg_frame = tk.Frame(chat_box, bg="white", pady=10)             # Add vertical padding and setting background color as white

# Configuration of the User chat
    # Color and image
    if sender == "user":                                            
        image = user_img
        prefix = "Student (You): "
        text_color = "blue"

        # Pack image on the right and text on the left within the frame
        tk.Label(msg_frame, text=prefix + message, fg=text_color, bg="white", wraplength=400, justify=tk.RIGHT).pack(side=tk.RIGHT, padx=5, anchor="n")
        tk.Label(msg_frame, image=image, bg="white").pack(side=tk.RIGHT, anchor="n")

        # Pack the frame to the right side of the chat box
        msg_frame.pack(anchor='e', fill='x', padx=5, pady=10)       # Increase vertical padding

# Configuration of the Bot chat
    # Color and image
    else:
        image = bot_img
        prefix = "Indiana James (Bot): "
        text_color = "green"  # Change bot text color here

        # Pack image on the left and text on the right within the frame
        tk.Label(msg_frame, image=image, bg="white").pack(side=tk.LEFT, anchor="n")
        tk.Label(msg_frame, text=prefix + message, fg=text_color, bg="white", wraplength=400, justify=tk.LEFT).pack(side=tk.LEFT, padx=5, anchor="n")

        # Pack the frame to the left side of the chat box
        msg_frame.pack(anchor='w', fill='x', padx=5, pady=10)       # Set up the vertical padding

    chat_box.window_create(tk.END, window=msg_frame)
    chat_box.insert(tk.END, "\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

# The main application window
root = tk.Tk()
root.title("Indiana James - History Chatbot")

# Window size
root.geometry("550x650")

# Scrolled text widget for the chat box with white background
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg="white")
chat_box.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Frame to hold the entry widget and send button
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10, fill=tk.X)

# Button to send messages
send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=5)

# Entry widget for user input
user_entry = tk.Entry(input_frame, width=80)
user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
user_entry.bind("<Return>", send_message)                           # Bind the Enter key to send messages

# Load images
try:
    user_img_path = "stu.png"
    bot_img_path = "indy.png"
    
    if not os.path.exists(user_img_path):                           # Error handling for the images
        raise FileNotFoundError(f"User image not found: {user_img_path}")
    
    if not os.path.exists(bot_img_path):                            # Error handling for the images
        raise FileNotFoundError(f"Bot image not found: {bot_img_path}")
    # Set up of the imagens in the chat
    user_img = ImageTk.PhotoImage(Image.open(user_img_path).resize((40, 40), Image.Resampling.LANCZOS))
    bot_img = ImageTk.PhotoImage(Image.open(bot_img_path).resize((40, 40), Image.Resampling.LANCZOS))
    print("Images loaded successfully.")

except Exception as e:
    print(f"Error loading images: {e}")
    user_img = None
    bot_img = None

# Greeting message of the bot
def start_chat():
    display_message("Hello, my name is Indiana James, let's learn some history today?", "bot")

start_chat()

# Application loop
root.mainloop()