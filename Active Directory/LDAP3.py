import tkinter as tk
from tkinter import messagebox
import random
import string
import hashlib
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE

# AD configuration
AD_SERVER = 'your_ad_server'
AD_USER = 'your_admin_user'
AD_PASSWORD = 'your_admin_password'
AD_SEARCH_BASE = 'DC=yourdomain,DC=com'

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to generate a random password
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Function to reset a user's password in AD
def reset_password(username, new_password=None):
    try:
        server = Server(AD_SERVER, get_info=ALL)
        conn = Connection(server, user=AD_USER, password=AD_PASSWORD, auto_bind=True)

        if not new_password:
            new_password = generate_random_password()

        conn.search(AD_SEARCH_BASE, f'(sAMAccountName={username})', attributes=['distinguishedName'])
        if not conn.entries:
            return f"User '{username}' not found in Active Directory."

        user_dn = conn.entries[0].distinguishedName.value
        new_password_quoted = f'"{new_password}"'
        unicode_pwd = new_password_quoted.encode('utf-16-le')

        conn.modify(user_dn, {'unicodePwd': [(MODIFY_REPLACE, [unicode_pwd])]})
        if conn.result['result'] == 0:
            return f"Password for user '{username}' has been reset successfully.\nNew password: {new_password}"
        else:
            return f"Failed to reset password for user '{username}'. Error: {conn.result['message']}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# GUI functions
def on_reset_button_click():
    username = username_entry.get()
    new_password = password_entry.get()
    if not new_password:
        new_password = None

    result = reset_password(username, new_password)
    messagebox.showinfo("Reset Password", result)

# Create the main window
root = tk.Tk()
root.title("AD Password Reset")

# Create and place widgets
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="New Password (leave blank to generate a random password):")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

reset_button = tk.Button(root, text="Reset Password", command=on_reset_button_click)
reset_button.pack(pady=20)

# Run the application
root.mainloop()
