import turtle
def face():
    turtle.speed(0)
    turtle.fillcolor("aqua")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0,85)
    turtle.pendown()
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

def righteye():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(50,105)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(50,120)
    turtle.pendown()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(50,130)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

def lefteye():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-50,105)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-50,120)
    turtle.pendown()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-50,130)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

def mouth():
    turtle.speed(0)
    turtle.setheading(270)
    turtle.penup()
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.setheading(0)
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.forward(80)
    turtle.left(270)
    turtle.circle(-40,180)
    turtle.end_fill()




def main():
    face()
    righteye()
    lefteye()
    mouth()
    stop=input("wtv")

main()