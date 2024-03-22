
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
z = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(z)
    global reps
    reps = 0
    canvas.itemconfig(timer, text=f"{WORK_MIN}:00")
    title_label.configure(text="Timer",fg=GREEN)
    check_marks.configure(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        countdown(work_sec)
        title_label.configure(text="Work",fg=GREEN)
    elif reps == 8:
        countdown(long_break_sec)
        title_label.configure(text="Break",fg=RED)
    else:
        countdown(short_break_sec)
        title_label.configure(text="Break",fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(time):
    global reps,z
    sec = str(time % 60)
    if len(sec) == 1:
        sec = "0"+sec
    min = str(time // 60)
    if len(min) == 1:
        min = "0"+min
    t = min+":"+sec
    canvas.itemconfig(timer,text=t)
    if time > 0:
        z = window.after(1000,countdown,time-1)
    else:
        start_timer()
        l = ["✔" for i in range(reps//2)]
        txt = ''.join(l)
        check_marks.configure(text=txt)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
window.grid()


title_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,36,"bold"), bg=YELLOW)
title_label.grid(row=0,column=1)
canvas = Canvas(bg=YELLOW,height=224,width=200,highlightthickness=0)
img = PhotoImage(file="tomato.png")                 # you need this to get hold of picture
canvas.create_image(100,112,image=img)              # image is not string here it's actual file
timer = canvas.create_text(100,120,text="25:00",font=("Courier",36,"bold"), fill="white")
canvas.grid(row=1,column=1)



check_marks = Label(font=(FONT_NAME,12,"bold"),fg=GREEN,bg=YELLOW,pady=20)
check_marks.grid(row=2,column=1)
start_btn = Button(text="Start",bg="white",command=start_timer)
start_btn.grid(row=2,column=0)
reset_btn = Button(text="Reset", bg="white",command=reset_timer)
reset_btn.grid(row=2,column=2)
window.mainloop()