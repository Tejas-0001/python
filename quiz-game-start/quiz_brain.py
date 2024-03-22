class QuizBrain:
    def __init__(self,questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):

        q = self.question_list[self.question_number].text
        a = self.question_list[self.question_number].answer
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {q} (True/False) ?\n")
        self.check_answer(a,choice)


    def check_answer(self,a,choice):
            if a.lower() == choice.lower():
                print(f"you are correct the answer is {a}")
                self.score += 1
            else:
                print(f"incorrect !! correct answer is {a}")
            print(f"your current score is{self.score}/{self.question_number}\n\n")


    def still_has_q(self):
        return self.question_number < len(self.question_list)

