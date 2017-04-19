import turtle
screen = turtle.Screen()
screen.screensize(600, 600)

prey = turtle.Turtle()
prey.penup()
prey.speed("slowest")
prey.fd(45)
prey.setheading(180)

wolf = turtle.Turtle()
wolf.penup()
wolf.speed("slowest")
wolf.goto(45, 45)


prey.fd(45)
print(wolf.distance(prey.pos()))

if (wolf.distance(prey.pos()) <= 64):
    wolf.goto(prey.pos())

turtle.mainloop()