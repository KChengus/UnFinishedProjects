
from Question import Question


class Celebs(Question):

    def __init__(self):
        self.questionList = self.getQuestionFromFile(self.__str__() + ".txt")

    def __str__(self):
        return "Celebs"