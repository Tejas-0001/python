from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for items in question_data:
    question_bank.append(Question(items["text"],items["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_q():
    quiz.next_question()

print("quiz completed")
print(f"Your final score is {quiz.score}/{quiz.question_number}")