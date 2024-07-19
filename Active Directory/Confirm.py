import tkinter as tk
from tkinter import messagebox

class ConfirmationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Confirmation Code")
        self.root.geometry("400x300")

        self.setup_ui()

    def setup_ui(self):
        self.container = tk.Frame(self.root, bg="#f0f0f0")
        self.container.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.container, text="Enter the Confirmation Code", font=("Arial", 18), pady=20)
        self.label.pack()

        self.input_frame = tk.Frame(self.container)
        self.input_frame.pack()

        self.code_inputs = []
        for _ in range(6):
            code_input = tk.Entry(self.input_frame, width=3, font=("Arial", 24), justify='center')
            code_input.pack(side=tk.LEFT, padx=5)
            vcmd = (self.root.register(self.validate_digit), '%P')
            code_input.config(validate="key", validatecommand=vcmd)
            self.code_inputs.append(code_input)

        self.confirm_button = tk.Button(self.container, text="Confirm", bg="#28a745", fg="white", font=("Arial", 16), pady=10, command=self.confirm_code)
        self.confirm_button.pack(pady=20)

        self.success_frame = tk.Frame(self.container)
        self.success_frame.pack()

        self.checkmark_canvas = tk.Canvas(self.success_frame, width=50, height=50, bg="#f0f0f0", bd=0, highlightthickness=0)
        self.checkmark_canvas.pack()
        self.draw_checkmark()

        self.success_label = tk.Label(self.success_frame, text="Code Confirmed!", font=("Arial", 16), pady=10)
        self.success_label.pack()

        self.hide_success_message()

    def validate_digit(self, new_value):
        if new_value.isdigit() and len(new_value) <= 1:
            return True
        else:
            return False

    def confirm_code(self):
        code = ''.join([entry.get() for entry in self.code_inputs])
        if len(code) == 6:
            self.show_success_message()
        else:
            messagebox.showwarning("Incomplete Code", "Please enter the complete 6-digit code.")

    def show_success_message(self):
        self.success_frame.pack()
        self.confirm_button.config(state=tk.DISABLED)

    def hide_success_message(self):
        self.success_frame.pack_forget()
        self.confirm_button.config(state=tk.NORMAL)

    def draw_checkmark(self):
        self.checkmark_canvas.create_oval(5, 5, 45, 45, outline="#28a745", width=5)
        self.checkmark_canvas.create_line(15, 30, 25, 40, 35, 20, fill="#28a745", width=5)

# Correct usage
if __name__ == "__main__":
    root = tk.Tk()  # Create Tkinter root window
    app = ConfirmationApp(root)
    root.mainloop()
