import tkinter as tk
from tkinter import messagebox

class UsernameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enter Username")
        self.root.geometry("400x200")
        self.root.config(bg="#f0f0f0")

        self.setup_ui()

    def setup_ui(self):
        self.container = tk.Frame(self.root, bg="#fff", padx=20, pady=20)
        self.container.pack(pady=20, expand=True)

        self.label = tk.Label(self.container, text="Enter Your Username", font=("Arial", 18), bg="#fff")
        self.label.pack(pady=10)

        self.username_input = tk.Entry(self.container, font=("Arial", 16), width=30, bd=1, relief="solid")
        self.username_input.pack(pady=10)

        self.submit_button = tk.Button(self.container, text="Submit", bg="#28a745", fg="white", font=("Arial", 16), command=self.submit_username)
        self.submit_button.pack(pady=10)

    def submit_username(self):
        username = self.username_input.get()
        if username:
            messagebox.showinfo("Username Submitted", f"Username: {username}")
        else:
            messagebox.showwarning("No Username", "Please enter a username.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UsernameApp(root)
    root.mainloop()
