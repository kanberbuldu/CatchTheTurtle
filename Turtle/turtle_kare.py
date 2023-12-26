import turtle


draw_screen = turtle.Screen()
draw_screen.bgcolor("light blue")
draw_screen.title("Kare Çizimi")

instance_turtle = turtle.Turtle()

for i in range(4):
    instance_turtle.left(90)
    instance_turtle.forward(200)

turtle.done()


