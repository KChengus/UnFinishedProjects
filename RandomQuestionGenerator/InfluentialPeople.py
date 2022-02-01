from Question import Question
class InfluentialPeople(Question):
    def getRandomQuestion(self):
        self.readQuestionFile(self.__str__() + ".txt")

    def __str__(self):
        return "InfluentialPeople"
