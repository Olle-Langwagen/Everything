import turtle
t = turtle.Turtle()
def rect(x,y,s):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for i in range(4):
        t.forward(s)
        t.right(90)
    t.end_fill()
rect(50,50,100)
turtle.exitonclick()
