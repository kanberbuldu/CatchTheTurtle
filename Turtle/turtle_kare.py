import turtle


draw_screen = turtle.Screen()
draw_screen.bgcolor("light blue")
draw_screen.title("Kare Çizimi")

turtle_instance = turtle.Turtle()

for i in range(4):
    turtle_instance.left(90)
    turtle_instance.forward(200)

turtle.done()


