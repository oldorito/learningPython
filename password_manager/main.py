from tkinter import *
from tkinter import messagebox
import random
import json

FONT = ("Arial", 10, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    if len(pass_entry.get()) == 0:
        pass_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    name = name_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "name": name,
            "password": password,
        }
    }

    if len(website) == 0 or len(name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning!", message="invalid data")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            name_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- FIND PASS ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            name = data[website]["name"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email/Username: {name}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Super Cool Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)
name_label = Label(text="Email/Username:", font=FONT)
name_label.grid(column=0, row=2)
pass_label = Label(text="Password:", font=FONT)
pass_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()
name_entry = Entry(width=50)
name_entry.grid(column=1, row=2, columnspan=2)
pass_entry = Entry(width=32)
pass_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)
pass_gen_button = Button(text="Generate Password", command=generate_password)
pass_gen_button.grid(column=2, row=3)
add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
