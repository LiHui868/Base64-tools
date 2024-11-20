#Author: lihui(Kris Li)
#Date: 2024-11-21 



import tkinter as tk
from tkinter import messagebox
import base64

def encode_base64():
    try:
        input_text = input_text_box.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to encode!")
            return
        encoded = base64.b64encode(input_text.encode("utf-8")).decode("utf-8")
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, encoded)
    except Exception as e:
        messagebox.showerror("Error", f"Encoding failed: {str(e)}")

def decode_base64():
    try:
        input_text = input_text_box.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Warning", "Please enter Base64 text to decode!")
            return
        decoded = base64.b64decode(input_text.encode("utf-8")).decode("utf-8")
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, decoded)
    except Exception as e:
        messagebox.showerror("Error", f"Decoding failed: {str(e)}")

def clear_text():
    input_text_box.delete("1.0", tk.END)
    output_text_box.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Base64 Encoder/Decoder Tool")
root.geometry("500x400")

# Input field
input_label = tk.Label(root, text="Input:", font=("Arial", 12))
input_label.pack(pady=5)
input_text_box = tk.Text(root, height=7, width=60)
input_text_box.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encode_button = tk.Button(button_frame, text="Encode", command=encode_base64, width=10)
encode_button.grid(row=0, column=0, padx=10)

decode_button = tk.Button(button_frame, text="Decode", command=decode_base64, width=10)
decode_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_text, width=10)
clear_button.grid(row=0, column=2, padx=10)

# Output field
output_label = tk.Label(root, text="Output:", font=("Arial", 12))
output_label.pack(pady=5)
output_text_box = tk.Text(root, height=7, width=60)
output_text_box.pack(pady=5)

# Main loop
root.mainloop()
