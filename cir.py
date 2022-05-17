class Circle:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.color = "black"
    def getXY(self):
        return self.x, self.y
    def getColor(self):
        return self.color
    def setColor (self, color):
        self.color = color

