class Canvas:

    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width

    def make(self):
        pass


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.y = y
        self.x = x

    def draw(self, canvas):
        pass


class Square:

    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw(self):
        pass