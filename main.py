from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 5)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = letters_list + numbers_list + symbols_list

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    # for char in password_list:
    #     password += char

    if password_entry.get() != '':
        password_entry.delete(0, END)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


def save_details():
    website_url = web_entry.get()
    fieldinp2 = email_entry.get()
    password = password_entry.get()

    data = {website_url: {'email': fieldinp2, 'password': password}}

    is_ok_to_save = messagebox.askokcancel("Confirm details before saving", "Do you want to save the entered details?")

    if is_ok_to_save:
        if website_url == '' or fieldinp2 == '' or password == '':
            messagebox.showwarning("Mandatory fields", "Mandatory details cannot be left blank")
        else:
            try:
                with open('Passwords.json', 'r') as f:
                    # f = open('Passwords.json', 'r')
                    # line = f"'website': {website_url} | 'email': {fieldinp2} | 'username': {fieldinp2} | 'password': {password}\n"
                    dt = json.load(f)
                    dt.update(data)
                with open('Passwords.json', 'w') as f:
                    # f = open('Passwords.json', 'w')
                    json.dump(dt, f, indent=4)
            except FileNotFoundError:
                with open('Passwords.json', 'w') as f:
                    json.dump(data, f, indent=4)
            web_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            web_entry.focus()
            messagebox.showinfo("Confirmation", "Details saved successfully")


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=2, row=2)

web_label = Label(text="Website:")
web_label.grid(column=1, row=3)

emailuserLabel = Label(text="Email/Username:")
emailuserLabel.grid(column=1, row=4)

password_label = Label(text="Password:")
password_label.grid(column=1, row=5)

web_entry = Entry(width=52)
web_entry.focus()
web_entry.grid(column=2, row=3, columnspan=2)


email_entry = Entry(width=52)
email_entry.grid(column=2, row=4, columnspan=2)

password_entry = Entry(width=52)
password_entry.grid(column=2, row=5, columnspan=2)

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(column=3, row=5)

empty_label = Label()
empty_label.grid(column=2, row=6)

button = Button(text="Add", width=45, command=save_details)
button.grid(column=2, row=7, columnspan=2)

window.mainloop()
