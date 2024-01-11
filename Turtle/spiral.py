import turtle


turtle_screeen = turtle.Screen()
turtle_screeen.title("Hortum Efekti")

turtle_ins = turtle.Turtle()
turtle_ins.speed(11)

turtle_colors = ["red","blue","white","yellow","orange","green"]

for i in range(50):
    turtle_ins.color(turtle_colors[i % 6])
    turtle_ins.circle( 2 * i)
    turtle_ins.left(i / 50)
    turtle_ins.circle(-2 * i)
    turtle_ins.left(i / 50)












turtle.done()

