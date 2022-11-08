class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        question_text = self.questions_list[self.question_number - 1].text
        answer = self.questions_list[self.question_number - 1].answer
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {question_text} True or False?")
        self.check_answer(user_answer, answer)

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print('Correct!')
            self.score += 1
            print(f"your score is {self.score}")

        else:
            print('Wrong!')
        print(f"The correct answer is {answer}")
