import tkinter as tk
from tkinter import scrolledtext

# Function to get chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        'hi': "Hello! How can I help you today?",
        'hello': "Hello! How can I help you today?",
        'hey': "Hello! How can I help you today?",
        'how are you?': "I'm just a program, so I don't have feelings, but thanks for asking! How can I assist you?",
        'what is your name?': "I am a simple chatbot created to answer your questions!",
        'bye': "Goodbye! Have a great day!",
        'what can you do?': "I can answer your basic questions. Try asking me about my name, how I am, or what I can do.",
        'how does this work?': "Just type your questions, and I'll try to respond based on my programming."
    }

    return responses.get(user_input, "I'm sorry, I don't understand that question. Can you please ask something else?")

# Function to handle sending messages
def send_message():
    user_input = user_entry.get()
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    chat_window.insert(tk.END, "Chatbot: " + chatbot_response(user_input) + "\n\n")
    chat_window.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Simple Chatbot")

# Create chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_window.config(state=tk.DISABLED)
chat_window.pack(pady=10, padx=10)

# Create user input entry box
user_entry = tk.Entry(root, width=80)
user_entry.pack(pady=10, padx=10)
user_entry.bind("<Return>", lambda event: send_message())

# Create send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

# Start GUI
root.mainloop()