import tkinter as tk
from tkinter import messagebox

class GenerateResetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CESC LOGIN")
        self.root.geometry("400x400")

        self.setup_ui()

    def setup_ui(self):
        self.container = tk.Frame(self.root, bg="#f0f0f0")
        self.container.pack(fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.container, text="Welcome to CESC", font=("Arial", 18), pady=20)
        self.title_label.pack()

        # Add Username Section
        self.add_username_frame = tk.Frame(self.container)
        self.add_username_frame.pack()

        self.username_entry = tk.Entry(self.add_username_frame, width=30, font=("Arial", 14))
        self.username_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_username_button = tk.Button(self.add_username_frame, text="Add Username", bg="#007bff", fg="white", font=("Arial", 14), command=self.add_username)
        self.add_username_button.grid(row=0, column=1, padx=10, pady=10)

        # Buttons Section
        self.button_frame = tk.Frame(self.container)
        self.button_frame.pack()

        self.generate_button = tk.Button(self.button_frame, text="Generate", bg="#28a745", fg="white", font=("Arial", 14), command=self.generate_content)
        self.generate_button.grid(row=0, column=0, padx=10, pady=10)

        self.reset_button = tk.Button(self.button_frame, text="Reset", bg="#dc3545", fg="white", font=("Arial", 14), command=self.reset_content)
        self.reset_button.grid(row=0, column=1, padx=10, pady=10)

        # Content Area
        #self.content_area = tk.Frame(self.container, bg="#f9f9f9", bd=2, relief=tk.SOLID)
        #self.content_area.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    def add_username(self):
        username = self.username_entry.get().strip()

        if username:
            username_label = tk.Label(self.content_area, text=f"Username: {username}", font=("Arial", 14), pady=5)
            username_label.pack()
            self.username_entry.delete(0, tk.END)  # Clear input field
        else:
            messagebox.showwarning("Empty Username", "Please enter a username.")

    def generate_content(self):
        # You can customize the content generation logic here if needed
        pass

    def reset_content(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GenerateResetApp(root)
    root.mainloop()
