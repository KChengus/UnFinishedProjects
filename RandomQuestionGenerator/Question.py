from abc import ABC, abstractmethod
class Question:

    def getQuestionFromFile(self, fileName):
        text = ""
        try:

            with open( "QuestionMap/" +fileName, "r") as f:
                text = f.read()

        except Exception as e:
            print(e)
        return text.split("\n")[:-1]

    @abstractmethod
    def getRandomQuestion(self):
        pass


    @abstractmethod
    def __str__(self):
        pass
