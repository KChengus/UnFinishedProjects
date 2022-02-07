from Question import Question
class Fashion(Question):

    def __init__(self):
        self.questionList = self.getQuestionFromFile(self.__str__() + ".txt")

    def __str__(self):
        return "Fashion"

if __name__ == "__main__":
    c = Fashion()
    c.getRandomQuestion()   