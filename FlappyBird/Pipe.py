class Pipe:
    def __init__(self, width, height, xPos, yPos):
        self.updateSize(width, height)
        self.updatePos(xPos, yPos)
    
    def updateSize(self, width, height):
        self.width = width
        self.height = height
    
    def updatePos(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos