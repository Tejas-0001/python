from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz:QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)
        self.answer = ""

        self.score = Label(text="Score: 0/10", font=("Arial",16,"italic"),bg=THEME_COLOR,fg="white")
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.t = self.canvas.create_text(150,125,text="Questions ^^",font=("Arial",16,"italic"),fill=THEME_COLOR,width=280)

        self.c_img = PhotoImage(file="./images/true.png")
        self.true = Button(text="", image=self.c_img, command=self.correct,highlightthickness=0,bd=0)
        self.true.grid(row=2,column=0)

        self.w_img = PhotoImage(file="./images/false.png")
        self.false = Button(text="", image=self.w_img, command=self.incorrect,highlightthickness=0,bd=0)
        self.false.grid(row=2, column=1)

        self.game()


        self.window.mainloop()


    def correct(self):
        self.answer = "True"
        self.true.configure(state=DISABLED)
        self.false.configure(state=DISABLED)
        self.check()

    def incorrect(self):
        self.answer = "False"
        self.true.configure(state=DISABLED)
        self.false.configure(state=DISABLED)
        self.check()

    def check(self):
        if self.quiz.check_answer(self.answer):
            self.canvas.config(bg="green")
            self.window.after(1000, func=self.game)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, func=self.game)

    def game(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.true.configure(state=ACTIVE)
            self.false.configure(state=ACTIVE)
            self.score.configure(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            txt = self.quiz.next_question()
            self.canvas.itemconfig(tagOrId=self.t, text=txt)
        else:
            self.canvas.itemconfig(tagOrId=self.t,text="End of Quiz")
            messagebox.showinfo(title="Game Over",
                                message=f"Your Final score is {self.quiz.score}/{self.quiz.question_number}")


