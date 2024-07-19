import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import random
import os

def generate_qr():
    text = qr_text.get()
    if len(text) > 0:
        random_number = random.randint(100000, 999999)  # Generate 6-digit random number
        qr_data = text + "\n" + str(random_number)  # Concatenate the text and the random number
        
        qr_img = qrcode.make(qr_data)
        qr_img.save("qrcode.png")

        img = Image.open("qrcode.png")
        img = img.resize((150, 150), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        qr_image_label.config(image=img)
        qr_image_label.image = img
        img_box.pack()
    else:
        messagebox.showwarning("Input Error", "Please enter a text or URL.")
        qr_text_entry.config(bg="red")
        qr_text_entry.after(1000, lambda: qr_text_entry.config(bg="white"))

root = tk.Tk()
root.title("QR Code Generator")

# Container
container = tk.Frame(root, bg="white", padx=35, pady=25)
container.pack(pady=50)

# Title
title = tk.Label(container, text="Enter your text or URL", font=("Poppins", 15), bg="white")
title.pack()

# Text Entry
qr_text = tk.StringVar()
qr_text_entry = tk.Entry(container, textvariable=qr_text, font=("Poppins", 12), bd=1, relief="solid", highlightthickness=0)
qr_text_entry.pack(pady=(10, 20), ipady=5, ipadx=5)

# QR Code Image Box
img_box = tk.Frame(container, bg="white")
img_box.pack(pady=10)
qr_image_label = tk.Label(img_box, bg="white")
qr_image_label.pack()

# Generate Button
generate_btn = tk.Button(container, text="Generate QR Code", command=generate_qr, font=("Poppins", 12), bg="#494eea", fg="white", bd=0, relief="solid", highlightthickness=0)
generate_btn.pack(pady=20, ipady=10, ipadx=10)

root.mainloop()

# Clean up the generated QR code image after the program closes
if os.path.exists("qrcode.png"):
    os.remove("qrcode.png")
