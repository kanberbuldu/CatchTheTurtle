import turtle

t_s = turtle.Screen()
t_s.title("Yin Yang")

turtle_instance = turtle.Turtle()

turtle_instance.begin_fill()
turtle_instance.fillcolor("black")
turtle_instance.circle(50,180)
turtle_instance.circle(-50,180)
turtle_instance.circle(-100,180)
turtle_instance.end_fill()
turtle_instance.circle(-100,180)


turtle_instance.teleport(2,60)
turtle_instance.begin_fill()
turtle_instance.fillcolor("black")
turtle_instance.circle(-15)
turtle_instance.end_fill()

turtle_instance.teleport(2,170)
turtle_instance.begin_fill()
turtle_instance.fillcolor("white")
turtle_instance.circle(-15)
turtle_instance.end_fill()
turtle_instance.hideturtle()

turtle.done()
