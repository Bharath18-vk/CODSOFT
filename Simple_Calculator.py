import tkinter as tk
from tkinter import messagebox

# Functions for calculations
def add(a, b):
    return a + b

def product(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
        return None

def difference(a, b):
    return a - b

# Function to handle calculations
def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        operation = operator.get()

        if operation == "+":
            result.set(add(a, b))
        elif operation == "-":
            result.set(difference(a, b))
        elif operation == "*":
            result.set(product(a, b))
        elif operation == "/":
            result_value = divide(a, b)
            if result_value is not None:
                result.set(result_value)
        else:
            messagebox.showwarning("Invalid Operation", "Please select a valid operator.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")
root.resizable(False, False)

# Create variables
entry1 = tk.StringVar()
entry2 = tk.StringVar()
operator = tk.StringVar()
result = tk.StringVar()

# Layout for inputs and buttons
tk.Label(root, text="Enter First Number:", font=("Helvetica", 12)).pack(pady=5)
tk.Entry(root, textvariable=entry1, font=("Helvetica", 12), width=20).pack()

tk.Label(root, text="Enter Second Number:", font=("Helvetica", 12)).pack(pady=5)
tk.Entry(root, textvariable=entry2, font=("Helvetica", 12), width=20).pack()

tk.Label(root, text="Select Operation:", font=("Helvetica", 12)).pack(pady=5)
operation_frame = tk.Frame(root)
operation_frame.pack(pady=5)

tk.Radiobutton(operation_frame, text="Add (+)", variable=operator, value="+", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(operation_frame, text="Subtract (-)", variable=operator, value="-", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(operation_frame, text="Multiply (*)", variable=operator, value="*", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(operation_frame, text="Divide (/)", variable=operator, value="/", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)

tk.Button(root, text="Calculate", command=calculate, font=("Helvetica", 12), bg="#4caf50", fg="white").pack(pady=10)
tk.Label(root, text="Result:", font=("Helvetica", 12)).pack(pady=5)
tk.Entry(root, textvariable=result, font=("Helvetica", 12), state="readonly", width=20).pack()

# Run the application
root.mainloop()
