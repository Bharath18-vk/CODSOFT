import tkinter as tk
from tkinter import ttk, messagebox


def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        task_list.insert("", "end", values=(task,))
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"'{task}' added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")


def remove_task():
    selected_item = task_list.selection()
    if selected_item:
        for item in selected_item:
            task = task_list.item(item, "values")[0]
            tasks.remove(task)
            task_list.delete(item)
        messagebox.showinfo("Success", "Task(s) removed successfully!")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")


def clear_tasks():
    task_list.delete(*task_list.get_children())
    tasks.clear()
    messagebox.showinfo("Success", "All tasks cleared!")


def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()


tasks = []

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x400")
root.configure(bg="#f0f0f0")


header = tk.Label(
    root,
    text="To-Do List",
    font=("Helvetica", 18, "bold"),
    bg="#3498db",
    fg="white",
    pady=10,
)
header.pack(fill=tk.X)


input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

task_entry = ttk.Entry(input_frame, width=40, font=("Helvetica", 12))
task_entry.pack(side=tk.LEFT, padx=10)

add_button = ttk.Button(input_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)


columns = ("Task",)
task_list = ttk.Treeview(root, columns=columns, show="headings", height=12)
task_list.heading("Task", text="Task")
task_list.pack(pady=10)


style = ttk.Style()
style.configure(
    "Treeview",
    font=("Helvetica", 12),
    rowheight=25,
    background="#e8f8f5",
    fieldbackground="#e8f8f5",
)
style.configure(
    "Treeview.Heading",
    font=("Helvetica", 14, "bold"),
    background="#45b39d",
    foreground="Blue",
)


button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

remove_button = ttk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=10)

clear_button = ttk.Button(button_frame, text="Clear All", command=clear_tasks)
clear_button.pack(side=tk.LEFT, padx=10)

exit_button = ttk.Button(button_frame, text="Exit", command=exit_app)
exit_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
