from abc import ABC, abstractmethod
class Question:

    def readQuestionFile(self, fileName):
        try:
            text = ""
            with open( "QuestionMap\\" +fileName, "r") as f:
                text = f.read()

            print(text.split("\n"))
        except Exception as e:
            print(e)

    @abstractmethod
    def getRandomQuestion(self):
        pass


    @abstractmethod
    def __str__(self):
        pass
