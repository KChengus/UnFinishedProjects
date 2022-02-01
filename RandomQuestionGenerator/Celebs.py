
from Question import Question


class Celebs(Question):
    def getRandomQuestion(self):
        self.readQuestionFile(self.__str__() + ".txt")

    def __str__(self):
        return "Celebs"