import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List App")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        # Entry for new task
        self.task_entry = tk.Entry(root, font=('Arial', 14))
        self.task_entry.pack(pady=10, padx=10, fill='x')

        # Add Task button
        tk.Button(root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white").pack(pady=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, font=('Arial', 12), selectbackground="#cce5ff")
        self.task_listbox.pack(padx=10, pady=10, fill='both', expand=True)

        # Buttons frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Mark as Done", command=self.mark_done, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)

        # Load tasks from file
        self.load_tasks()

        # Save tasks on window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Input Error", "Task cannot be empty!")
        else:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_done(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)
            if not task.startswith("✔️ "):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, "✔️ " + task)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r", encoding='utf-8') as f:
                for line in f:
                    self.task_listbox.insert(tk.END, line.strip())

    def save_tasks(self):
        with open(TASKS_FILE, "w", encoding='utf-8') as f:
            tasks = self.task_listbox.get(0, tk.END)
            for task in tasks:
                f.write(task + "\n")

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
