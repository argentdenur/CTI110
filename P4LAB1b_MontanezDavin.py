import turtle
print(turtle)
wn = turtle.Screen()
wn.bgcolor('black')
turtle.color('red')
turtle.pensize(10)

# Draw first initial: D
turtle.left(90)
turtle.down()
turtle.forward(75)
turtle.right(45)
for x in range(180):
    turtle.forward(1.55)
    turtle.right(1.55)

# Draw second initial: M
turtle.right(40)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.right(90)
turtle.penup()
turtle.forward(120)
turtle.pendown()
turtle.right(90)
turtle.forward(100)
turtle.left(180)
turtle.forward(100)
turtle.right(150)
turtle.forward(100)
turtle.left(150)
turtle.forward(100)
turtle.right(150)
turtle.forward(100)

