from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def Save_Passwords():
    with open("myPassword.txt", "a") as f:
        data_web = Website_entry.get()
        data_email = Email_entry.get()
        data_password = Password_entry.get()
        summary_data = f"{data_web} | {data_email} | {data_password}\n"
        Website_entry.delete(0,END)
        Email_entry.delete(0,END)
        Email_entry.insert(0,"ledangkhoa11a1@gmail.com")
        Password_entry.delete(0,END)
        f.write(summary_data)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo setup
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo_password.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Create and set position for labels
Website_label = Label(text="Website:")
Website_label.grid(column=0, row=1, sticky="W")
Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2, sticky="W")
Password_label = Label(text="Password:")
Password_label.grid(column=0, row=3, sticky="W")

# Create and set position for entries
Website_entry = Entry(width=35)
Website_entry.grid(column=1, row=1, columnspan=2,sticky="W")
Website_entry.focus()

Email_entry = Entry(width=35)
Email_entry.grid(column=1, row=2, columnspan=2, sticky="W")
Email_entry.insert(0, "ledangkhoa11a1@gmail.com")

Password_entry = Entry(width=21)
Password_entry.grid(column=1, row=3, sticky="W")

# Create and set position for buttons
Generate_btn = Button(text="Generate Password", width=14)
Generate_btn.grid(column=2, row=3, sticky="W")

Add_btn = Button(text="Add", width=36, command=Save_Passwords)
Add_btn.grid(column=1, row=4, columnspan=3, sticky="W")

window.mainloop()
