import tkinter as tk
from tkinter import messagebox
class ToDoList:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.task_listbox = tk.Listbox(root, width=40)
        self.task_listbox.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(padx=10, pady=10)

        self.create_button = tk.Button(root, text="Create Task", command=self.create_task)
        self.create_button.pack(padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(padx=10, pady=10)
    def create_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
    def update_task(self):
        task_id = self.task_listbox.curselection()
        if task_id:
            task_id = task_id[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[task_id] = new_task
                self.task_listbox.delete(task_id)
                self.task_listbox.insert(task_id, new_task)
                self.task_entry.delete(0, tk.END)
    def delete_task(self):
        task_id = self.task_listbox.curselection()
        if task_id:
            task_id = task_id[0]
            self.tasks.pop(task_id)
            self.task_listbox.delete(task_id)
def main():
    root = tk.Tk()
    root.title("To-Do List")
    todo_list = ToDoList(root)
    root.mainloop()
if __name__ == "__main__":
    main()