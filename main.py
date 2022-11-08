from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for item in question_data:
    new_question = Question(item['text'], item['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print('You complete the quiz')
print(f"Your final score is {quiz.score} out of {quiz.question_number}")