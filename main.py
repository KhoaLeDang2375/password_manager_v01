from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def Generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [ random.choice(letters)for x in range(nr_letters) ]
    password_number = [ random.choice(numbers)for x in range(nr_numbers) ]
    password_symbol = [ random.choice(symbols)for x in range(nr_symbols) ]

    password_list=password_letter+password_number+password_symbol
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def Save_Passwords():
        data_web = website_entry.get()
        data_email = email_entry.get()
        data_password =password_entry.get()
        new_data ={data_web:{
         "email":data_email,
         "password":data_password}
         }
        #Website_name or Password is empty
        if(len(data_web) == 0 or len(data_password) == 0):
             messagebox.askretrycancel(title="Warning!!",message="Please don't leave any fileds empty!")
        #Website name and Password isn't empty
        else:
            is_ok=messagebox.askyesnocancel(title="Oops", message=f" These are details entered: \n Email;{data_email}\n Password:{data_password}\nIs it ok to save your password?")
            if is_ok:
                    with open("myPassword.json", "w") as data_file:
                        json.dump(new_data,data_file,indent=4)
                        website_entry.delete(0,END)
                        email_entry.delete(0,END)
                        email_entry.insert(0,"")
                        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo_password.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ledangkhoa11a1@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=Generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=Save_Passwords)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
