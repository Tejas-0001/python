from tkinter import *
import string
import random
from tkinter import messagebox
import pyperclip
import json

def search_result():
    web = website_input.get().lower()
    try:
        with open("password.json","r") as f:
            result = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title=web,message="you have not saved anything yet")
    except json.decoder.JSONDecodeError:
        messagebox.showerror(title=web, message="no data for the website found")

    else:
        try:
            messagebox.showinfo(title=f"search result for {web}",message=f"username={result[web]['email']}\npassword={result[web]['password']}")
        except KeyError:
            messagebox.showerror(title=web,message="No data for this website has been found")




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    alphabets = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    length = 8
    no_len = 4
    sym_len = 4

    chars = random.choices(alphabets, k=length)
    nos= random.choices(numbers, k=no_len)
    sym = random.choices(symbols, k=sym_len)
    password = chars + nos + sym
    random.shuffle(password)
    password = ''.join(password)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():

    if len(website_input.get()) == 0:
        messagebox.showerror(title="Error",message="Website field cannot be empty")
    elif len(password_input.get()) == 0:
        messagebox.showerror(title="Error", message="Password field cannot be empty")
    else:
        is_okay = messagebox.askokcancel(title=f"{website_input.get()}",message=f"Details entered:\nemail:{username_input.get()}\npassword: {password_input.get()}\nSave details ? ")

        if is_okay:
            # with open("password.txt","a") as f:
            # json.dump() - write
            #json.load() - read
            #json.update() - update

            new_data = {
                website_input.get().lower() :
                    {
                        "email":username_input.get(),
                        "password":password_input.get()
                    }
            }

            try:
                with open("password.json","r") as f:
                    #reading json
                    data = json.load(f)

            except FileNotFoundError:
                with open("password.json","w") as f:
                    json.dump(new_data,f,indent=4)
            except json.decoder.JSONDecodeError:
                with open("password.json","w") as f:
                    json.dump(new_data,f,indent=4)

            else:
                data.update(new_data)
                with open("password.json","w") as f:
                    json.dump(data,f,indent=4)

            finally:
                messagebox.showinfo(title="Process Done", message="All details have been saved")
                website_input.delete(0,END)
                password_input.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password-Manager")
window.configure(pady=100,padx=50)
window.grid()

canvas = Canvas(width=200,height=200,highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=0,columnspan=3)

website = Label(text="Website:")
website.grid(row=1,column=0)
website_input = Entry(width=21)
website_input.grid(row=1,column=1)
website_input.focus()

search = Button(text="Search",command=search_result,width=13)
search.grid(row=1,column=2)

username = Label(text="username:")
username.grid(row=2,column=0)
username_input = Entry(width=40)
username_input.grid(row=2,column=1,columnspan=2)
username_input.insert(0,"Tejas@gmail.com")

password_label = Label(text="password:")
password_label.grid(row=3,column=0)
password_input = Entry(width=21)
password_input.grid(row=3,column=1)
password_btn = Button(text="Generate Password",command=gen_password)
password_btn.grid(row=3,column=2)
add_btn = Button(text="Add",width=36,command=save_to_file)
add_btn.grid(row=4,column=1,columnspan=2)

window.mainloop()