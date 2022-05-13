import tkinter as tk
from RQG import RQG
import random
import os
import webScrapingImages
from PIL import ImageTk, Image
rqg = RQG()
root = tk.Tk()
root.geometry("500x500")

"""
Improvements

* Optimise code
    - make it clearner
    - utilize classes
    - remove unnecessary code
    - add comments throughout the code

* Extra functions
    - Make a solution button where it shows the solution to the current picture



"""
# display variables
btnWidth = 20;   


canvas= tk.Canvas(root, width= 400, height= 300)
canvas.pack()

def btnClicked():
    print("Button clicked")


def displayCategories():
    toplvl = tk.Toplevel(root)
    toplvl.geometry("300x200")
    def categoryChosen(strNum):
        rqg.pickCategoryGUI(int(strNum))
        toplvl.destroy()

    tk.Label(toplvl, text=rqg.categoryInTextForm()).pack()

    # MAKE A LOOP FOR THIS V
    tk.Button(toplvl, text="0", width=btnWidth, command=lambda: categoryChosen("0")).pack()  
    tk.Button(toplvl, text="1", width=btnWidth, command=lambda: categoryChosen("1")).pack()  
    tk.Button(toplvl, text="2", width=btnWidth, command=lambda: categoryChosen("2")).pack()  
    tk.Button(toplvl, text="3", width=btnWidth, command=lambda: categoryChosen("3")).pack()  

# image functions
def getImagePath(imageFolder):
    pathToImageFolder = f"imgs/{imageFolder}/"
    if not os.path.isdir(pathToImageFolder):
        webScrapingImages.run(imageFolder)
    path =  pathToImageFolder + random.choice(os.listdir(pathToImageFolder))
    print(path)
    return path


def generateImage(imageFolder): 
    global img
    

    img = Image.open(getImagePath(imageFolder))
    img = img.resize((400, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    canvas.create_image(10, 10, anchor = tk.NW, image=img)
    

    print("creating image")   
    

def getQuestion():
    category = rqg.getRandomCategoryFromChosenCategories()
    question = random.choice(category.questionList)
    print(question)
    generateImage(question)




lbl = tk.Label(root, text="this is just a temporary place holder")
lbl.pack()

displayCatBtn = tk.Button(root, text="display category", width=btnWidth, command=displayCategories)
displayCatBtn.pack()

getQuestionBtn = tk.Button(root, text="get question", command=getQuestion)
getQuestionBtn.pack()

root.mainloop()