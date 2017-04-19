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

#Functions for "go right" both turtle and dog
def go_right_turtle(step):
    new_range = turtle.xcor() + 15
    if new_range >= x:
        go_left_turtle(step)
    else:
        turtle.setheading(0)
        turtle.forward(step)

def go_right_dog(step):
    new_range = dog.xcor() + 15
    if new_range >= x:
        go_left_dog(step)
    else:
        dog.setheading(0)
        dog.forward(step)

#Functions for "go up" both turtle and dog
def go_up_turtle(step):
    new_range = turtle.ycor() + 15
    if new_range >= y:
        edge = new_range - y
        new_step = step - edge
    else:
        new_step = step

    turtle.setheading(90)
    turtle.forward(new_step)

def go_up_dog(step):
    new_range = dog.ycor() + 15
    if new_range >= y:
        edge = new_range - y
        new_step = step - edge
    else:
        new_step = step

    dog.setheading(90)
    dog.forward(new_step)

#Functions for "go left" both turtle and dog
def go_left_turtle(step):
    new_range = turtle.xcor() - 15
    if new_range <= -x:
        go_right_turtle(step)
    else:
        turtle.setheading(180)
        turtle.forward(step)

def go_left_dog(step):
    new_range = dog.xcor() - 15
    if new_range <= -x:
        go_right_dog(step)
    else:
        dog.setheading(180)
        dog.forward(step)

#Functions for "go down" both turtle and dog
def go_down_turtle(step):
    new_range = turtle.ycor() - 15
    if new_range <= -y:
        go_up_turtle(step)
    else:
        turtle.setheading(270)
        turtle.forward(step)

def go_down_dog(step):
    new_range = dog.ycor() - 15
    if new_range <= -y:
        go_up_dog(step)
    else:
        dog.setheading(270)
        dog.forward(step)

def make_random_walk(step_size, step_number):
    move_dict_turtle = {1: go_up_turtle,
                 2: go_right_turtle,
                 3: go_left_turtle,
                 4: go_down_turtle
                 }
    move_dict_dog = {1: go_up_dog,
                     2: go_right_dog,
                     3: go_left_dog,
                     4: go_down_dog
                     }
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(random.randint(1,300),random.randint(1,300))
    turtle.showturtle()

    dog.hideturtle()
    dog.setpos(random.randint(1, 300), random.randint(1, 300))
    dog.showturtle()

    for _ in range(step_number):
        move_in_a_direction_turtle = move_dict_turtle[random.randint(1, 4)]
        move_in_a_direction_turtle(step_size)
        move_in_a_direction_dog = move_dict_dog[random.randint(1, 4)]
        move_in_a_direction_dog(step_size)

step_size = 15
step_number = 1000
make_random_walk(step_size, step_number)

turtle.mainloop()