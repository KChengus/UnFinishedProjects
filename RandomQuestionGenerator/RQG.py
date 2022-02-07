import random
from Cars import Cars
from Celebs import Celebs
from Fashion import Fashion
from Math import Math
from History import History
from InfluentialPeople import InfluentialPeople

class RQG:
    
    categories = [Cars, Fashion, Celebs, InfluentialPeople]
    chosenCategoryIndex = list()
    def __init__(self):
        pass

    def categoryInTextForm(self):
        text = ""
        for i, category in enumerate(self.categories):
            text += f"{i}. {category()}\n"
        return text

    def pickCategoryGUI(self, num):
        if 0 <= num < len(self.categories):
            self.chosenCategoryIndex.append(num)
        print("Chose category number", num)


    def pickCategoryInTerminal(self):
        try:
            while True:
                self.printCategories()
                a = int(input("input Category number"))
                if a >= len(self.categories):
                    print("enter a number between: 0 and", len(self.categories))
                else:
                    print(self.categories[a]())
                    self.chosenCategoryIndex.append(a)
        except Exception as e:
            print(e)
        
    def getRandomCategoryFromChosenCategories(self):
        
        n = random.choice(self.chosenCategoryIndex)
        return self.categories[n]()
        
        
    def mainRun(self):
        self.pickCategory()
        print(self.getRandomCategory())
        self.printCategories()
    


if __name__ == "__main__":
    RQG().mainRun()