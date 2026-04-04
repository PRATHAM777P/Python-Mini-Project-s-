import secrets
import string
import tkinter as tk
from tkinter import messagebox

# Word lists
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'blue', 'green']
nouns = ['apple', 'dragon', 'panda', 'hammer', 'duck', 'goat']

confusing_chars = "l1IO0"

# Password strength checker
def check_strength(password):
    strength = 0

    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if len(password) >= 12:
        strength += 1

    levels = ["Weak", "Medium", "Strong", "Very Strong", "Excellent"]
    strength_label.config(text=f"Strength: {levels[strength-1] if strength>0 else 'Weak'}")

# Generate password
def generate_password():
    length = length_var.get()

    chars = string.ascii_lowercase + string.digits + string.punctuation

    if uppercase_var.get():
        chars += string.ascii_uppercase

    if avoid_confusing_var.get():
        chars = ''.join(c for c in chars if c not in confusing_chars)

    if memorable_var.get():
        password = secrets.choice(adjectives) + secrets.choice(nouns) + str(secrets.randbelow(100))
    else:
        if length < 6:
            messagebox.showwarning("Warning", "Password length should be at least 6")
            return
        password = ''.join(secrets.choice(chars) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    check_strength(password)

# Save password
def save_password():
    password = password_entry.get()
    if password == "":
        messagebox.showwarning("Warning", "Generate a password first!")
        return

    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

    messagebox.showinfo("Saved", "Password saved!")

# Copy to clipboard
def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Toggle show/hide
def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Clear field
def clear_password():
    password_entry.delete(0, tk.END)
    strength_label.config(text="Strength:")

# GUI setup
root = tk.Tk()
root.title("🔐 PassForge Pro")
root.geometry("420x420")

# Length
tk.Label(root, text="Password Length:").pack()
length_var = tk.IntVar(value=12)
tk.Entry(root, textvariable=length_var).pack()

# Options
uppercase_var = tk.BooleanVar()
avoid_confusing_var = tk.BooleanVar()
memorable_var = tk.BooleanVar()
show_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).pack()
tk.Checkbutton(root, text="Avoid Confusing Characters", variable=avoid_confusing_var).pack()
tk.Checkbutton(root, text="Memorable Password (words)", variable=memorable_var).pack()
tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password).pack()

# Buttons
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack()

# Strength label
strength_label = tk.Label(root, text="Strength:")
strength_label.pack()

# Action buttons
tk.Button(root, text="Copy", command=copy_password).pack(pady=5)
tk.Button(root, text="Save", command=save_password).pack(pady=5)
tk.Button(root, text="Clear", command=clear_password).pack(pady=5)

root.mainloop()
