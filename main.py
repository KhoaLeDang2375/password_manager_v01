from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def Search_Websites():
    data_web=website_entry.get()
    try:
        with open("myPassword.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No data file found!")
            file=open("myPassword.json","w")
            file.close()
    else:
        if data_web in data:
            email=data[data_web]["email"]
            password=data[data_web]["password"]
            messagebox.showinfo(title=data_web,message=f"Email: {email}\nPassword:{password}")
        else:
             messagebox.showinfo(title="Error",message=f"Not exist website {data_web} in data file!")
       
              

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
        new_data ={
              data_web:{
         "email":data_email,
         "password":data_password}
         }
        #Website_name or Password is empty
        if len(data_web) == 0 or len(data_password) == 0:
            messagebox.showwarning(title="Warning!", message="Please don't leave any fields empty!")
        else:
            is_ok = messagebox.askyesnocancel(title="Confirm", message=f"These are the details entered:\nEmail: {data_email}\nPassword: {data_password}\nIs it okay to save?")
        
            if is_ok:
                    try:
                        with open("myPassword.json", "r") as data_file:
                            # Đọc dữ liệu cũ từ tệp
                            data = json.load(data_file)
                    except (FileNotFoundError, json.JSONDecodeError):
                        # Nếu tệp không tồn tại hoặc lỗi định dạng, tạo dữ liệu trống
                        data = {}
                    
                    # Cập nhật dữ liệu cũ với dữ liệu mới
                    data.update(new_data)

                    with open("myPassword.json", "w") as data_file:
                        # Lưu dữ liệu đã cập nhật
                        json.dump(data, data_file, indent=4)

                    # Xóa các mục nhập cũ trong các ô đầu vào
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
                    email_entry.insert(0, "ledangkhoa11a1@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=100)

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
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
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
Searched_btn=Button(text="Search",command=Search_Websites,width=13)
Searched_btn.grid(row=1,column=2)
window.mainloop()
