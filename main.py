import turtle

a = 5
print(a)

roshan_turt = turtle.Turtle()

# Use turtle module to draw a square
def makeSquare():
    roshan_turt.forward(100)
    roshan_turt.right(90)
    roshan_turt.forward(100)
    roshan_turt.right(90)
    roshan_turt.forward(100)
    roshan_turt.right(90)
    roshan_turt.forward(100)

makeSquare()
roshan_turt.forward(100)
makeSquare()
roshan_turt.forward(100)
makeSquare()
roshan_turt.forward(100)
makeSquare()
roshan_turt.forward(100)

turtle.done()