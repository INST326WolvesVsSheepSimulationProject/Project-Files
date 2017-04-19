#Import turtle and define the screen
import turtle
import random
x = 300
y = 300
screen = turtle.Screen()
screen.screensize(600, 600)

#Shows to border of the 600x600 window
test = turtle.Turtle()
test.penup()
test.fd(300)
test.pendown()
test.setheading(90)
test.fd(300)
test.setheading(180)
test.fd(600)
test.setheading(270)
test.fd(600)
test.setheading(0)
test.fd(600)
test.setheading(90)
test.fd(300)

#Imports the image, creates a turtle object "dog", and adds the image to dog
img_dog = r"C:\Users\andre\PycharmProjects\project\Dog.gif"
dog = turtle.Turtle()
screen.addshape(img_dog)
dog.shape(img_dog)
dog.penup()

def go_right(step):
    new_range = turtle.xcor() + 15
    if new_range >= x:
        go_left(step)
    else:
        turtle.setheading(0)
        turtle.forward(step)

def go_up(step):
    new_range = turtle.ycor() + 15
    if new_range >= y:
        edge = new_range - y
        new_step = step - edge
    else:
        new_step = step

    turtle.setheading(90)
    turtle.forward(new_step)


def go_left(step):
    new_range = turtle.xcor() - 15
    if new_range <= -x:
        go_right(step)
    else:
        turtle.setheading(180)
        turtle.forward(step)

def go_down(step):
    new_range = turtle.ycor() - 15
    if new_range <= -y:
        go_up(step)
    else:
        turtle.setheading(270)
        turtle.forward(step)

def make_random_walk(step_size, step_number):
    move_dict = {1: go_up,
                 2: go_right,
                 3: go_left,
                 4: go_down
                 }
    for _ in range(step_number):
        move_in_a_direction = move_dict[random.randint(1, 4)]
        move_in_a_direction(step_size)

step_size = 15
step_number = 1000
make_random_walk(step_size, step_number)

turtle.mainloop()
