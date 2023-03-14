from canvas import Canvas
from shapes import Rectangle, Square

canvas = Canvas(1000, 700, (255, 255, 255))
rectangle = Rectangle(50, 100, 200, 100, (55, 62, 75))
square = Square(200, 500, 100, (155, 200, 205))
rectangle.draw(canvas)
square.draw(canvas)
canvas.make('canvas.png')
