import turtle

window = turtle.Screen()

window.bgcolor("black")

turtle_pen = turtle.Pen()

turtle_pen.pencolor("white")

for counter in range(100):

    turtle_pen.forward(counter)

    turtle_pen.left(46)