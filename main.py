# Don't forget to follow Joshua Samuel Nichols :)

import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>/?"
    substitutions = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 'l': '7', 't': '7', 'E': '3'}

    # Start with a random length for the password between 12 and 16
    password_length = random.randint(12, 16)

    # Generate a basic password
    basic_password = ''.join(random.choice(chars + special_chars) for _ in range(password_length))

    # Substitute some letters
    substituted_password = ''.join(substitutions.get(c, c) for c in basic_password)

    # Display in the entry widget
    password_entry.delete(0, tk.END)
    password_entry.insert(0, substituted_password)

def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Password Copied", "Your password has been copied to the clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

# Create entry widget to display password
password_entry = tk.Entry(root, font=('Arial', 14), bd=0, bg='lightgray', width=22)
password_entry.pack(pady=20)

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Generate and Copy buttons
generate_button = tk.Button(button_frame, text="Generate Password", command=generate_password, font=('Arial', 14))
copy_button = tk.Button(button_frame, text="Copy", command=copy_to_clipboard, font=('Arial', 14))

generate_button.grid(row=0, column=0, padx=10)
copy_button.grid(row=0, column=1, padx=10)

# Set the window not resizable
root.resizable(False, False)

# Start the GUI
root.mainloop()
