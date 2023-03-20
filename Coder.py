#coder 
import tkinter as tk
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import pyperclip
import json
import os

# Load the GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Define the function to generate code based on user input
def generate_code():
    # Get the user input from the text box
    prompt = input_box.get("1.0", "end-1c")

    # Check if the prompt is already in the conversation history
    if prompt in conversation_history:
        # If it is, retrieve the generated code from the history
        generated_code = conversation_history[prompt]
    else:
        # If it's not, generate code using the GPT-2 model
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        output = model.generate(input_ids, max_length=1024, do_sample=True)
        generated_code = tokenizer.decode(output[0], skip_special_tokens=True)

        # Store the prompt and generated code in the conversation history
        conversation_history[prompt] = generated_code

        # Save the conversation history to a file
        with open("conversation_history.json", "w") as f:
            json.dump(conversation_history, f)

    # Display the generated code in the output box
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, generated_code)

# Define the function to copy the generated code to the clipboard
def copy_output():
    generated_code = output_box.get("1.0", "end-1c")
    pyperclip.copy(generated_code)

# Load the conversation history from a file, or create a new empty history if the file doesn't exist
if os.path.exists("conversation_history.json"):
    with open("conversation_history.json") as f:
        conversation_history = json.load(f)
else:
    conversation_history = {}

# Create the GUI window
window = tk.Tk()
window.title("Code Generator")

# Create the input box for the user to enter their prompt
input_box = tk.Text(window, height=10, width=50)
input_box.pack()

# Create the button to generate code
generate_button = tk.Button(window, text="Generate Code", command=generate_code)
generate_button.pack()

# Create the output box to display the generated code
output_box = tk.Text(window, height=10, width=50)
output_box.pack()

# Create the button to copy the generated code to the clipboard
copy_button = tk.Button(window, text="Copy Output", command=copy_output)
copy_button.pack()

# Start the GUI event loop
window.mainloop()


  
