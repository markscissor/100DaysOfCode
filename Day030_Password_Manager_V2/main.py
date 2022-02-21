import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found")
    else:
        try:
            email = data[website]['email']
            password = data[website]['password']
        except KeyError:
            messagebox.showinfo(message="No details for the website exists")
        else:
            messagebox.showinfo(message=f"Email/Username: {email}\nPassword: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    total_nr = nr_letters + nr_numbers + nr_symbols
    count_l = 0
    count_s = 0
    count_n = 0
    password_list = []

    while True:
        i = random.randint(1, 3)
        if i == 1 and count_l < nr_letters:
            password_list.append(random.choice(letters))
            count_l += 1
        elif i == 2 and count_s < nr_symbols:
            password_list.append(random.choice(symbols))
            count_s += 1
        elif i == 3 and count_n < nr_numbers:
            password_list.append(random.choice(numbers))
            count_n += 1

        if len(password_list) == total_nr:
            break

    password = "".join(password_list)
    pass_entry.delete(0, 'end')
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')
            web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
web_label = tk.Label(text="Website:")
web_label.grid(row=1, column=0)
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pass_label = tk.Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entries
web_entry = tk.Entry(width=20)
email_entry = tk.Entry(width=35)
pass_entry = tk.Entry(width=20)
web_entry.grid(row=1, column=1, sticky=tk.NW, pady=5)
web_entry.focus()
email_entry.grid(row=2, column=1, columnspan=2, sticky=tk.NW, pady=5)
email_entry.insert(0, "username@gmail.com")
pass_entry.grid(row=3, column=1, sticky=tk.NW, pady=5)

# Buttons
search_button = tk.Button(text="Search", width=15, command=find_password, bg="blue")
search_button.grid(row=1, column=2, sticky=tk.NW, padx=10)
generate_button = tk.Button(text="Generate Password", width=17, command=generate_password)
generate_button.grid(row=3, column=2, sticky=tk.NW, padx=10)
add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=tk.NW, pady=5)


window.mainloop()
