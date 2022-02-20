import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


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
    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\n"
                                                      f"Password: {password}\nIs it ok to save?")

        if is_ok:
            entry = f"{website} | {email} | {password}\n"
            with open("data.txt", "a") as file:
                file.write(entry)
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
web_entry = tk.Entry(width=35)
email_entry = tk.Entry(width=35)
pass_entry = tk.Entry(width=21)
web_entry.grid(row=1, column=1, columnspan=2, sticky=tk.NW)
web_entry.focus()
email_entry.grid(row=2, column=1, columnspan=2, sticky=tk.NW)
email_entry.insert(0, "username@gmail.com")
pass_entry.grid(row=3, column=1, sticky=tk.NW)

# Buttons
generate_button = tk.Button(text="Generate Password", width=17, command=generate_password)
generate_button.grid(row=3, column=2, sticky=tk.NW)
add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=tk.NW)


window.mainloop()
