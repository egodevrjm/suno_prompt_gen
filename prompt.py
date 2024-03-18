import json
import random
import tkinter as tk
from tkinter import ttk
import pyperclip

# Load the JSON data
with open("prompt.json", "r") as file:
    data = json.load(file)

# Function to generate the prompt
def generate_prompt():
    genre1 = random.choice(data["music_genres"])
    genre2 = random.choice(data["music_genres"])
    story = random.choice(data["story_ideas"])
    prompt = f"'{genre1}' and '{genre2}' about  {story}"
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, prompt)

# Function to copy the prompt to the clipboard
def copy_to_clipboard():
    prompt = result_text.get(1.0, tk.END).strip()
    pyperclip.copy(prompt)

# Create the main window
window = tk.Tk()
window.title("Prompt Generator")
window.geometry("500x350")

# Create and pack the widgets
title_label = ttk.Label(window, text="Prompt Generator", font=("Arial", 16))
title_label.pack(pady=20)

generate_button = ttk.Button(window, text="Generate Prompt", command=generate_prompt)
generate_button.pack(pady=10)

result_text = tk.Text(window, wrap=tk.WORD, width=60, height=6)
result_text.pack(pady=10)

copy_button = ttk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Start the main event loop
window.mainloop()