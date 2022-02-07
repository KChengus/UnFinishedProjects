import tkinter as tk
from RQG import RQG
import random
rqg = RQG()
root = tk.Tk()
root.geometry("500x500")

def btnClicked():
    print("Button clicked")

def getQuestion():
    category = rqg.getRandomCategoryFromChosenCategories()
    print(random.choice(category.questionList))

def displayCategories():
    toplvl = tk.Toplevel(root)
    toplvl.geometry("300x200")
    def categoryChosen(strNum):
        rqg.pickCategoryGUI(int(strNum))
        toplvl.destroy()

    tk.Label(toplvl, text=rqg.categoryInTextForm()).pack()

    # MAKE A LOOP FOR THIS V
    tk.Button(toplvl, text="0", command=lambda: categoryChosen("0")).pack()  
    tk.Button(toplvl, text="1", command=lambda: categoryChosen("1")).pack()  
    tk.Button(toplvl, text="2", command=lambda: categoryChosen("2")).pack()  
    tk.Button(toplvl, text="3", command=lambda: categoryChosen("3")).pack()  
#def clickedGenerateQuestion():
lbl = tk.Label(root, text="this is just a temporary place holder")
lbl.pack()

anotherbtn = tk.Button(root, text="another button")
anotherbtn.pack()

displayCatBtn = tk.Button(root, text="display category", command=displayCategories)
displayCatBtn.pack()

getQuestionBtn = tk.Button(root, text="get question", command=getQuestion)
getQuestionBtn.pack()

btn = tk.Button(root, text="button", command=btnClicked)
btn.pack()
root.mainloop()