import turtle


turtle_screen = turtle.Screen()
turtle_screen.title("User Control")
turtle_screen.bgcolor("light blue")



turtle_ins = turtle.Turtle()


def user_forward():
    turtle_ins.forward(100)
def user_turnleft():
    turtle_ins.left(10)
def user_turnright():
    turtle_ins.right(10)

def user_home():
    user_penup()
    turtle_ins.home()
    user_pendown()

def user_penup():
    turtle_ins.penup()
def user_pendown():

    turtle_ins.pendown()

def user_clear_screen():
    turtle_ins.clear()



turtle_screen.listen()
turtle_screen.onkeypress(user_forward,"space")
turtle_screen.onkeypress(user_turnleft,"Left")
turtle_screen.onkeypress(user_turnright,"Right")
turtle_screen.onkeypress(user_clear_screen,"c")
turtle_screen.onkeypress(user_home,"h")












turtle.mainloop()