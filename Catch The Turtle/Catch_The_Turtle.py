import turtle
import time
import random

turtle_screen = turtle.Screen()
turtle_screen.title("Catch The Turtle")
turtle_screen.bgcolor("light blue")





def turtle_tt():

    t = 20
    while t > 0:
        turtle_t = turtle.Turtle()

        turtle_t.hideturtle()
        turtle_t.penup()
        turtle_t.setposition(0, 230)
        turtle_t.pendown()
        turtle_t.pencolor("red")
        turtle_t.write((f"Time: {t}" ),move=False,align="Center", font=("arial", 14, "bold"),)

        turtle_ins = turtle.Turtle(shape= "turtle",visible = False)
        #turtle_ins.turtle()
        turtle_ins.color("green")
        turtle_ins.speed(0.1)
        y_1 = random.randint(-600, 600)
        y_2 = random.randint(-300, 300)
        turtle_ins.penup()
        turtle_ins.teleport(y_1,y_2)
        turtle_ins.showturtle()

        #turtle_ins.teleport(y_1, y_2)
        turtle_ins.pendown()

        time.sleep(1)

        turtle_t.clear()
        t -= 1
        turtle_ins.hideturtle()



        if t == 0:
            turtle_t.write("Game Over !",font=("arial",14,"bold"))





def score_write():
    turtle_score = turtle.Turtle()
    turtle_score.teleport(x=-50,y=260)
    turtle_score.isvisible="false"
    turtle_score.pencolor("dark blue")
    turtle_score.hideturtle()
    turtle_score.write("Score:",font=("arial",14,"bold"))


def score_point():
    turtle_score = turtle.Turtle()
    turtle_score.teleport(x=15, y=260)
    turtle_score.isvisible = "false"
    turtle_score.pencolor("dark blue")
    turtle_score.hideturtle()
    turtle_score.write("", font=("arial", 14, "bold"))




score_point()
score_write()
turtle_tt()



turtle.mainloop()