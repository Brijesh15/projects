import math

class geometry():
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        self.x += deltaX
        self.y += deltaY

class circle(geometry):
    def __init__(self, x=0.0, y=0.0, radius=1.0):
        super(circle,self).__init__(x,y)
        self.radius = radius
    def calArea(self):
        return math.pi*self.radius**2

class rectangle(geometry):
    def __init__(self, x=0.0, y=0.0, width=1.0, height=1.0):
        super(rectangle,self).__init__(x,y)
        self.width = width
        self.height = height
    def calArea(self):
        return self.width = width * self.height = height

class square(rectangle):
    def __init__(self, x=0.0, y=0.0, sidelenght=1.0):
        super(square,self).__init__(x,y,sidelenght,sidelenght)
