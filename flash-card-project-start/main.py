BACKGROUND_COLOR = "#B1DDC6"
FRONT = "./images/card_front.png"
BACK = "./images/card_back.png"
counter = 0
temporary = -1

from tkinter import *
import pandas
import random

"""data handling"""
data = pandas.read_csv("./data/russian_words.csv")
rus = data.Russian
eng = data.English
correct_words = []
wrong_words = []

def correct():
    if eng[temporary] in correct_words or wrong_words:
        pass
    else:
        correct_words.append(eng[temporary])
        # print(correct_words)

def wrong():
    if eng[temporary] in wrong_words or correct_words:
        pass
    else:
        wrong_words.append(eng[temporary])
        # print(wrong_words)

"""functioning"""

def rand():
    global temporary,eng,correct_words,wrong_words
    temporary = random.randint(1,999)
    if eng[temporary] in correct_words or wrong_words:
        temporary = random.randint(1,999)

def change():
    global counter,rus,eng,temporary
    # print(counter)
    if counter % 2 == 1:
        card.configure(file=BACK)
        # print(temporary)
        canvas.itemconfig(tagOrId=txt,text=eng[temporary])
        window.after(3000,change)
    else:
        card.configure(file=FRONT)
        rand()
        # print(temporary)
        canvas.itemconfig(tagOrId=txt,text=rus[temporary])
        window.after(5000,change)
    counter += 1
    # print("adafasfaa")




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
right = Button(image=card_right,highlightthickness=0,command=correct)
right.grid(row=1,column=0)

card_wrong = PhotoImage(file="./images/wrong.png")
wrong = Button(image=card_wrong,highlightthickness=0,command=wrong)
wrong.grid(row=1,column=2)




window.after(1000,change)


window.mainloop()

print("these are the words you couldn't get")
print(wrong_words)