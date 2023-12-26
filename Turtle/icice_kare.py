import turtle

turtle_win  = turtle.Screen()
turtle_win.title("İç içe kareler")
turtle_win.bgcolor("light green")


turtle_intense = turtle.Turtle()
turtle_intense.color("red")
turtle_intense.speed(5)

def kare (size):
    for i in range(4):
        turtle_intense.forward(size)
        turtle_intense.left(90)
        size  -= 5

sayac = 0

for i in range(7):
    sayac+=20
    kare(150 - sayac)



turtle.done()