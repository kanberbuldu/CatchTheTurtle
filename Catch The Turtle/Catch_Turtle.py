import turtle
import random

score = 0

screen = turtle.Screen()
screen.title("Catch the Turtle")
screen.bgcolor("light blue")
FONT = ("arial",15,"bold")
gride_size = 10
turtle_list =[]


#Score turtle

turtle_score = turtle.Turtle()

#countdown_turtle
count_down_turtle = turtle.Turtle()
def setup_turtle_score():
    turtle_score.hideturtle()


    turtle_score.color("dark blue")

    top_height = screen.window_height() / 2
    y = top_height * 0.9
    turtle_score.penup()
    turtle_score.setposition(0, y)
    turtle_score.write(arg="Score: 0",move= False, align= "Center",font=FONT)



def make_turtle(x,y):
    t = turtle.Turtle()
    def handle_click(x, y):
        global score
        score +=1
        turtle_score.clear()
        turtle_score.write(arg=f"Score: {score}",move= False, align= "Center",font=FONT)
        #print(x,y)


    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.color("dark green")
    t.shapesize(1.5,1.5)
    t.goto(x * gride_size,y * gride_size)
    turtle_list.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates= [20,10,0,-10,-20]


def setup_turtle():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)



def hide_turtle():
    for t in turtle_list:
        t.hideturtle()

def random_show():
    hide_turtle()
    random.choice(turtle_list).showturtle()

    screen.ontimer(random_show, 500)

def count_down(time):
    count_down_turtle.hideturtle()
    count_down_turtle.color("black")
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    count_down_turtle.penup()
    count_down_turtle.setposition(0, y-30)
    count_down_turtle.clear()


    if time >0:
        count_down_turtle.clear()
        count_down_turtle.write(arg=f"Time: {time} ", move=False, align="Center", font=FONT)
        screen.ontimer(lambda: count_down(time -1 ),1000)
    else:
        count_down_turtle.clear()
        hide_turtle()
        count_down_turtle.write(arg="Game Over! ", move=False, align="Center", font=FONT)



turtle.tracer(0)

setup_turtle_score()
setup_turtle()
hide_turtle()
random_show()
count_down(15)
turtle.tracer(1)

turtle.mainloop()