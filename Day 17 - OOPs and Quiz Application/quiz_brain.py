class QuizBrain:

    def __init__(self,question_list):
        self.question_list=question_list
        self.question_number=0
        self.score=0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number+=1
        ans=input(f"Q.{self.question_number} : {question.question} ? True / False")
        self.check_answer(ans,question.correctAnswer)

    def still_has_questions(self):
        return len(self.question_list)> self.question_number

    def check_answer(self,answer,correct_answer):
        if answer.lower() == correct_answer.lower() :
            print("You are right")
            self.score+=1
        else :
            print("Oops ! Better Luck Next Time ")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score} / {self.question_number}")
        print("\n")

    def getScore(self):
        return [self.score,len(self.question_list)]