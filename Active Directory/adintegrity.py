import random
import string
import hashlib
import json
import tkinter as tk
from tkinter import messagebox
from ldap3 import Server, Connection, ALL, NTLM
import mysql.connector
from mysql.connector import Error

# Active Directory configuration
ad_server = 'ldap://your_ad_server'
ad_domain = 'your_ad_domain'
ad_base_dn = 'OU=users,DC=example,DC=com'
ad_user_dn = 'CN=binduser,OU=users,DC=example,DC=com'
ad_user_password = 'bindpassword'

# MySQL configuration
mysql_host = 'your_mysql_host'
mysql_user = 'mysql_user'
mysql_password = 'mysql_password'
mysql_database = 'your_database'

def ldap_authenticate(username, password):
    user_dn = f'{ad_domain}\\{username}'
    try:
        server = Server(ad_server, get_info=ALL)
        conn = Connection(server, user_dn, password, authentication=NTLM)
        if conn.bind():
            print(f'User {username} authenticated successfully')
            conn.unbind()
            return True
        else:
            print(f'Failed to authenticate user {username}')
            return False
    except Exception as e:
        print(f'LDAP authentication error: {e}')
        return False

def mysql_connect():
    try:
        connection = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        )
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection
    except Error as e:
        print(f'MySQL connection error: {e}')
        return None

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def read_user_data(file_path='users.json'):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_user_data(user_data, file_path='users.json'):
    with open(file_path, 'w') as file:
        json.dump(user_data, file, indent=4)

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def reset_password(username, new_password=None):
    user_data = read_user_data()

    if username not in user_data:
        return f"User '{username}' not found."

    if not new_password:
        new_password = generate_random_password()

    hashed_password = hash_password(new_password)
    user_data[username]['password'] = hashed_password

    write_user_data(user_data)
    return f"Password for user '{username}' has been reset.\nNew password: {new_password}"

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
        
    return pwd

def on_generate_button_click(length_entry, number_var, special_var, password_entry):
    try:
        min_length = int(length_entry.get())
        has_number = number_var.get()
        has_special = special_var.get()
        password = generate_password(min_length, has_number, has_special)
        animate_password_display(password, password_entry)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def animate_password_display(password, password_entry):
    password_entry.config(state=tk.NORMAL)
    password_entry.delete(0, tk.END)
    for i in range(len(password)):
        password_entry.insert(tk.END, password[i])
        password_entry.update()
        password_entry.after(100)
    password_entry.config(state=tk.DISABLED)

def check_password_strength(entry):
    password = entry.get()
    
    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])
    
    characters = [upper_case, lower_case, special, digits]
    
    length = len(password)
    
    score = 0
    
    with open('common.txt', 'r') as f:
        common = f.read().splitlines()
    
    if password in common:
        result = "Password was found in a common list. Score: 0 / 7"
        messagebox.showinfo("Result", result)
        return
    
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 20:
        score += 1
    if length > 17:
        score += 1
    
    if sum(characters) > 1:
        score += 1
    if sum(characters) > 2:
        score += 1
    if sum(characters) > 3:
        score += 1
    
    if score < 4:
        result = f"The password is quite weak! Score: {score} / 7"
    elif score == 4:
        result = f"The password is quite ok! Score: {score} / 7"
    elif score > 4 and score < 6:
        result = f"The password is pretty good! Score: {score} / 7"
    elif score > 6:
        result = f"The password is strong! Score: {score} / 7"
    
    messagebox.showinfo("Result", result)

def main():
    username = input('Enter username: ')
    choice = input('Enter "1" to generate password, "2" to reset password and check password strength: ')

    if choice == '1':
        root = tk.Tk()
        root.title("Password Generator with Animation")

        length_label = tk.Label(root, text="Minimum Password Length:")
        length_label.pack(pady=5)

        length_entry = tk.Entry(root)
        length_entry.pack(pady=5)
        length_entry.insert(0, "10")

        number_var = tk.BooleanVar()
        number_check = tk.Checkbutton(root, text="Include Numbers", variable=number_var)
        number_check.pack(pady=5)
        number_var.set(True)

        special_var = tk.BooleanVar()
        special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
        special_check.pack(pady=5)
        special_var.set(True)

        password_entry = tk.Entry(root, state=tk.DISABLED, width=40)
        password_entry.pack(pady=5)

        generate_button = tk.Button(root, text="Generate Password", command=lambda: on_generate_button_click(length_entry, number_var, special_var, password_entry))
        generate_button.pack(pady=20)

        root.mainloop()

    elif choice == '2':
        new_password = input('Enter new password (leave blank to generate a random password): ')
        if not new_password:
            new_password = None
        result = reset_password(username, new_password)
        print(result)

        root = tk.Tk()
        root.title("Password Strength Checker")

        label = tk.Label(root, text="Enter your password:")
        label.pack(pady=10)

        entry = tk.Entry(root, show="*")
        entry.pack(pady=10)

        button = tk.Button(root, text="Check Strength", command=lambda: check_password_strength(entry))
        button.pack(pady=10)

        root.mainloop()

if __name__ == "__main__":
    main()
