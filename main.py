from PIL import Image
import numpy as np


class Canvas:

    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.height, self.y:self.y + self.width] = self.color


class Square:

    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.side, self.y:self.y + self.side] = self.color


canvas = Canvas(1000, 700, (255, 255, 255))
rectangle = Rectangle(50, 100, 200, 100, (55, 62, 75))
square = Square(200, 500, 100, (155, 200, 25))
rectangle.draw(canvas)
square.draw(canvas)
canvas.make('canvas.png')
