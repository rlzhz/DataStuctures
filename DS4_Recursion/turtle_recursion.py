import turtle
import time

import time
# 同时设置pencolor=color1, fillcolor=color2
# turtle.color("red","yellow")
# turtle.begin_fill()
# for _ in range(50):
#     turtle.forward(200)
#     turtle.left(170)
#     turtle.end_fill()
#
# turtle.mainloop()

# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()
# def drawSpiral(myTurtle,lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#     myTurtle.right(90)
#     drawSpiral(myTurtle,lineLen-5)

myTurtle = turtle.Turtle()

myTurtle.forward(100)

drawSpiral(myTurtle,100)