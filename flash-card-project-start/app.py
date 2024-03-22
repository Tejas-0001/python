BACKGROUND_COLOR = "#B1DDC6"
FRONT = "./images/card_front.png"
BACK = "./images/card_back.png"
counter = 0
temporary = -1

from tkinter import *
import pandas
import random

"""data handling"""
try:
    data = pandas.read_csv("./data/words_not_learnt.csv")
    words = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("./data/russian_words.csv")
    words = data.to_dict(orient="records")



# print(words)
rus = data["Russian"].to_list()
# print(rus)
eng = data["English"].to_list()

curr_card = {}


"""functioning"""

def flip():

    global curr_card
    card.configure(file=BACK)
    canvas.itemconfig(tagOrId=txt,text=curr_card["English"],fill="white")


def next_card():

    global curr_card,z
    window.after_cancel(z)
    curr_card  = random.choice(words)
    print(curr_card)
    # print(curr_card["Russian"])
    card.configure(file=FRONT)
    canvas.itemconfig(tagOrId=txt, text=curr_card["Russian"],fill="black")
    z = window.after(3000,flip)


"""
for these 2 fn next card correct and wrong replace it with 1 saying is_known

def is_known():
words.remove(curr_card)
next_card()


"""
def next_card_correct():

    global curr_card,z,rus,eng
    window.after_cancel(z)
    rus.remove(curr_card["Russian"])
    eng.remove(curr_card["English"])
    curr_card  = random.choice(words)
    print(curr_card)
    # print(curr_card["Russian"])
    card.configure(file=FRONT)
    canvas.itemconfig(tagOrId=txt, text=curr_card["Russian"],fill="black")
    z = window.after(3000,flip)

def next_card_wrong():

    global curr_card,z
    window.after_cancel(z)
    curr_card  = random.choice(words)
    print(curr_card)
    # print(curr_card["Russian"])
    card.configure(file=FRONT)
    canvas.itemconfig(tagOrId=txt, text=curr_card["Russian"],fill="black")
    z = window.after(3000,flip)






"""UI"""

window = Tk()
window.title("Learn Russian")
window.configure(padx=50,pady=100,background=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card = PhotoImage(file=FRONT)
canvas.create_image(400,263,image=card)
txt = canvas.create_text(400,253,text="Starting ...",font=("Arial",36,"bold"))
canvas.grid(row=0,column=0,columnspan=3)


card_right = PhotoImage(file="./images/right.png")
right = Button(image=card_right,highlightthickness=0,command=next_card_correct) #make is known function and from there call next card
right.grid(row=1,column=0)

card_wrong = PhotoImage(file="./images/wrong.png")
wrong = Button(image=card_wrong,highlightthickness=0,command=next_card_wrong)
wrong.grid(row=1,column=2)

z = window.after(1000,next_card)




window.mainloop()

"""file handling"""

d = {
    "Russian":rus,
    "English":eng
}

f = pandas.DataFrame(d)
f.to_csv("./data/words_not_learnt.csv",index=False)


"""

but a better way is just save it as we move along the program

so in is_okay fn add these lines
d = pandas.DataFrame(data)
d.to_csv("./data/words_not_learnt.csv",index=False)



"""


# print("these are the words you couldn't get")
# print(wrong_words)