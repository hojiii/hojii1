class QuizBrain:

    def __init__(self, q_list):
        self.questionumber = 0
        self.questionlist = q_list
        self.answer_score = 0

    def still_has_question(self):
        return self.questionumber < len(self.questionlist)

    def next_question(self):
        current_question = self.questionlist[self.questionumber]
        self.questionumber+=1
        user_answer = input(f"Q.{self.questionumber}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.answer_score += 1
        else:
            print("That.s wrong.")
        print(f"The answer was : {correct_answer}.")
        print(f"Your current score is : {self.answer_score}/{self.questionumber}")
        print("\n")