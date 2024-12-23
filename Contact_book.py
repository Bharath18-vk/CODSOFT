import tkinter as tk
from tkinter import messagebox

Contacts = {}

def add_contact():
    name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone_number and email and address:
        Contacts[name] = {"phone_number": phone_number, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def view_contacts():
    contacts_list.delete(0, tk.END)
    for name, details in Contacts.items():
        contacts_list.insert(tk.END, f"{name}: {details['phone_number']}")

def search_contact():
    search_query = search_entry.get()
    if search_query:
        for name, details in Contacts.items():
            if name == search_query or details['phone_number'] == search_query:
                messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {details['phone_number']}\nEmail: {details['email']}\nAddress: {details['address']}")
                return
        messagebox.showwarning("Not Found", "Contact not found!")
    else:
        messagebox.showwarning("Input Error", "Enter a name or phone number to search!")

def update_contact():
    name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name in Contacts:
        Contacts[name] = {"phone_number": phone_number, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showwarning("Not Found", "Contact not found!")

def delete_contact():
    name = name_entry.get()
    if name in Contacts:
        del Contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showwarning("Not Found", "Contact not found!")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

# Input Fields
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(frame)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(frame)
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Address:").grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(frame)
address_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

# Search Field
tk.Label(root, text="Search:").pack(pady=5)
search_entry = tk.Entry(root)
search_entry.pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)

# Contact List
tk.Label(root, text="Contacts:").pack(pady=5)
contacts_list = tk.Listbox(root, height=10, width=50)
contacts_list.pack(pady=10)

view_contacts()

root.mainloop()
