from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import os
import pyperclip

FONT = ("Courier", 12, "normal")

def generate_password():
    """Generates a random password consisting of 8-9 letters + 2-3 numbers and 2-3 symbols
    then inserts the random password into the password entry field and finally copies the random password
    to the user clipboard so it can be used immediately"""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters = [choice(letters) for _ in range(randint(8, 10))]
    numbers = [choice(numbers) for _ in range(randint(2, 4))]
    symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letters + numbers + symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

def save_password():
    """Takes the user input and first validates it to ensure no fields are left blank, if this condition
    is satisfied the user is asked to confirm the details they have entered with a pop-up message confirmation
    to which they can select 'ok' or 'cancel'. Select 'ok' = details are saved in a newly created 'Saved_Logins'
    .txt file if one does not exist, otherwise the details are appended to a new line within the file. The website
    and password fields are then reset to blanks"""

    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_login = f"{website} | {email_username} | {password}"

    if len(email_username) < 1 or len(password) < 1 or len(website) < 1:
        messagebox.showinfo("Oops", "Please dont leave any fields empty!")
    else:
        proceed = messagebox.askokcancel(
            title=website, message=f"Email:{email_username} \nPassword:{password} \nProceed?"
        )
        if proceed:
            if not os.path.exists("Saved_Logins"):
                with open("Saved_Logins", "a+") as f:
                    f.write(new_login + "\n")
            else:
                with open("Saved_Logins", "a+") as f:
                    f.write(new_login + "\n")

            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(height=200,width=200, bg="white", highlightthickness=0 )
mypass_logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=mypass_logo)
canvas.grid(column=1,row=0)

# labels
website_label = Label(text="Website:",  bg="white")
website_label.grid(column=0,row=1)

email_username_label = Label(text="Email/Username:",  bg="white")
email_username_label.grid(column=0,row=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0,row=3)

# entries
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=40)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "email@address.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# buttons
gen_pass_button = Button(
    text="Generate Password", bg="white", highlightthickness=0, width=15, command=generate_password
)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=31, bg="white", padx=10, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()