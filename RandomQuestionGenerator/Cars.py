
from Question import Question


class Cars(Question):
    
    def __init__(self):
        self.questionList = self.getQuestionFromFile(self.__str__() + ".txt")

    def __str__(self):
        return "Cars"

if __name__ == "__main__":
    c = Cars()
    c.getRandomQuestion()   