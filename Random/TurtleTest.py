import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.penup()
t.hideturtle()
t.speed(100)
t.color("white")

t.setpos(-100, 100)

t.left(90)
t.pendown()
t.forward(35)

t.width(10)


t.setposition(-100,-50)
t.pendown()
t.right(180)
#Start
for i in range(90):
    t.forward(1)
    t.left(1)
#N

t.penup()
t.setpos(-100,-50)
t.forward(50)
t.pendown()
t.left(90)
t.forward(100)
t.right(145)
t.forward(120)
t.left(145)
t.forward(100)
t.penup()
t.right(90)
t.forward(30)
t.pendown()
#T
t.forward(70)
t.penup()
t.right(180)
t.forward(35)
t.left(90)
t.pendown()
t.forward(100)
t.penup()
#I
t.left(90)
t.forward(75)
t.left(90)
t.pendown()
t.forward(100)

#-
t.penup()
t.setpos(-100,135)
t.right(90)
t.pendown()
t.forward(75)


turtle.exitonclick()
