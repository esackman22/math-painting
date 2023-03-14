from canvas import Canvas
from shapes import Rectangle, Square


canvas_width = int(input('How wide would you like your canvas? '))
canvas_height = int(input('How tall would you like your canvas? '))
canvas_color = input('Would you like your canvas to be black or white? Enter b for black, w for white: ')
if canvas_color == 'b':
    canvas = Canvas(canvas_width, canvas_height, (0, 0, 0))
else:
    canvas = Canvas(canvas_width, canvas_height, (255, 255, 255))

while True:
    shape = input('Which shape would you like to draw, a square or a rectangle? Enter "quit" to quit: ')
    if shape == 'quit':
        break
    elif shape == 'rectangle':
        x = int(input('Enter rectangle x coordinate: '))
        y = int(input('Enter rectangle y coordinate: '))
        width = int(input('Enter rectangle width: '))
        height = int(input('Enter rectangle height: '))
        red = int(input('Enter red value (0-255): '))
        green = int(input('Enter green value (0-255): '))
        blue = int(input('Enter blue value (0-255): '))
        rectangle = Rectangle(x, y, width, height, (red, green, blue))
        rectangle.draw(canvas)
    else:
        x = int(input('Enter square x coordinate: '))
        y = int(input('Enter square y coordinate: '))
        side = int(input('Enter square side length: '))
        red = int(input('Enter red value (0-255): '))
        green = int(input('Enter green value (0-255): '))
        blue = int(input('Enter blue value (0-255): '))
        square = Square(x, y, side, (red, green, blue))
        square.draw(canvas)

canvas.make('canvas.png')