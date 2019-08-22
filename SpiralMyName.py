import turtle
turtle_pen = turtle.Pen()
window = turtle.Screen()
window.bgcolor("black")
window.title("Spiral My Name")
Colors = ['red','yellow','green','#1ec9a1','blue','#cc6e8c']
for spiral_length in range(300):
    color = Colors[spiral_length % 6]

    turtle_pen.pencolor(color)
    turtle_pen.forward(spiral_length)
    turtle_pen.left(90)