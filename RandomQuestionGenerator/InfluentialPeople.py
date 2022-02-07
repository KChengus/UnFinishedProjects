from Question import Question
class InfluentialPeople(Question):

    def __init__(self):
        self.questionList = self.getQuestionFromFile(self.__str__() + ".txt")


    def __str__(self):
        return "InfluentialPeople"
