import tkinter as tk
from tkinter import ttk, messagebox
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning("Invalid Input", "Password length must be at least 4 characters.")
            return

        uppercase_pool = string.ascii_uppercase
        lowercase_pool = string.ascii_lowercase
        number_pool = string.digits
        special_pool = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

        password = [
            random.choice(uppercase_pool),
            random.choice(lowercase_pool),
            random.choice(number_pool),
            random.choice(special_pool),
        ]

        combined_pool = uppercase_pool + lowercase_pool + number_pool + special_pool
        password += random.choices(combined_pool, k=length - 4)

        random.shuffle(password)

        password_output.set(''.join(password))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for password length.")


root = tk.Tk()
root.title("Password Generator")
root.geometry("450x350")
root.configure(bg="#2b2b2b")
root.resizable(False, False)

password_output = tk.StringVar()

header = tk.Label(
    root,
    text="Secure Password Generator",
    font=("Helvetica", 18, "bold"),
    bg="#4caf50",
    fg="white",
    pady=10,
)
header.pack(fill=tk.X)

frame = tk.Frame(root, bg="#383838", padx=10, pady=10)
frame.pack(pady=20)
 
length_label = tk.Label(frame, text="Password Length:", font=("Helvetica", 12, "bold"), bg="#383838", fg="#e0e0e0")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = ttk.Entry(frame, font=("Helvetica", 12), width=10)
length_entry.grid(row=0, column=1, padx=5, pady=5)


generate_button = tk.Button(
    frame,
    text="Generate Password",
    command=generate_password,
    font=("Helvetica", 10, "bold"),
    bg="#4caf50",
    fg="white",
    activebackground="#388e3c",
    activeforeground="white",
    relief="raised",
    bd=3,
)
generate_button.grid(row=1, column=0, columnspan=2, pady=15, ipadx=10)
output_label = tk.Label(
    root,
    text="Generated Password:",
    font=("Helvetica", 12, "bold"),
    bg="#2b2b2b",
    fg="#e0e0e0",
)
output_label.pack(pady=5)

output_entry = ttk.Entry(
    root,
    textvariable=password_output,
    font=("Helvetica", 12),
    state="readonly",
    width=30,
)
output_entry.pack()

exit_button = tk.Button(
    root,
    text="Exit",
    command=root.quit,
    font=("Helvetica", 10, "bold"),
    bg="#f44336",
    fg="white",
    activebackground="#d32f2f",
    activeforeground="white",
    relief="raised",
    bd=3,
)
exit_button.pack(pady=10, ipadx=20)

root.mainloop()
