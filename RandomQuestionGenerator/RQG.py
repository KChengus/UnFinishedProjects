import random
from Cars import Cars
from Celebs import Celebs
from Fashion import Fashion
from Math import Math
from History import History
from InfluentialPeople import InfluentialPeople

class RQG:
    
    categories = [Cars, Fashion, Celebs, InfluentialPeople]
    chosenCategoryIndex = []
    def __init__(self):
        pass

    def printCategories(self):
        for i, category in enumerate(self.categories):
            print(f"{i}. {category()}")

    def pickCategory(self):
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
        
    def getRandomCategory(self):
        n = random.randrange(0, len(self.categories))
        randomPickIndex = self.chosenCategoryIndex[n]
        return self.categories[randomPickIndex]()
        
        
    def mainRun(self):
        self.pickCategory()
        print(self.getRandomCategory())
    


if __name__ == "__main__":
    RQG().mainRun()