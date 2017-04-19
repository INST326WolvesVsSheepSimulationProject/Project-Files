#Survival simulation – Create animals that "live" in a simulated two-dimensional world.
#As you program each animal, you define the strategies that each animal uses to look
#for food to eat, fight for dominance, cooperate as a community, reproduce, etc.
#Your goal is for both your animal and the ecosystem to thrive.

#Currently playing around with the function for the second initial sheep "sheep2"
#def create_second_sheep():
    #sheep2 = turtle.Turtle()
    #sheep2.penup()
    #sheep2.hideturtle()
    #screen.addshape(img_sheep)
    #sheep2.shape(img_sheep)
    #sheep2.setpos(random.randint(1, 300), random.randint(1, 300))
    #sheep2.showturtle()

#Functions for "go right" for wolf, sheep and dog
def go_right_wolf(step):
    new_range = wolf.xcor() + 15
    if (wolf.distance(sheep_leader.pos()) <= 85):
        wolf.goto(sheep_leader.pos())
        sheep_leader.hideturtle()
        turtle.mainloop()
    elif new_range >= x:
        go_left_wolf(step)
    else:
        wolf.setheading(0)
        wolf.forward(step)

def go_right_dog(step):
    new_range = dog.xcor() + 15
    if (dog.distance(wolf.pos()) <= 85):
        dog.goto(wolf.pos())
        dog_on_wolf()
        turtle.mainloop()
    elif new_range >= x:
        go_left_dog(step)
    else:
        dog.setheading(0)
        dog.forward(step)

def go_right_sheep(step):
    new_range = sheep_leader.xcor() + 15
    if new_range >= x:
        go_left_sheep(step)
    else:
        sheep_leader.setheading(0)
        sheep_leader.forward(step)

#Functions for "go up" for wolf, sheep, and dog
def go_up_wolf(step):
    new_range = wolf.ycor() + 15
    if (wolf.distance(sheep_leader.pos()) <= 85):
        wolf.goto(sheep_leader.pos())
        sheep_leader.hideturtle()
        turtle.mainloop()
    elif new_range >= y:
        edge = new_range - y
        new_step = step - edge
    else:
        new_step = step

    wolf.setheading(90)
    wolf.forward(new_step)

def go_up_dog(step):
    new_range = dog.ycor() + 15
    if (dog.distance(wolf.pos()) <= 85):
        dog.goto(wolf.pos())
        dog_on_wolf()
        turtle.mainloop()
    elif new_range >= y:
        edge = new_range - y
        new_step = step - edge
    else:
        new_step = step

    dog.setheading(90)
    dog.forward(new_step)

def go_up_sheep(step):
    new_range = sheep_leader.ycor() + 15
    if new_range >= y:
        edge = new_range - y
        new_step = step - edge
    else:
        new_step = step

    sheep_leader.setheading(90)
    sheep_leader.forward(new_step)

#Functions for "go left" for wolf, sheep, and dog
def go_left_wolf(step):
    new_range = wolf.xcor() - 15
    if (wolf.distance(sheep_leader.pos()) <= 85):
        wolf.goto(sheep_leader.pos())
        sheep_leader.hideturtle()
        turtle.mainloop()
    elif new_range <= -x:
        go_right_wolf(step)
    else:
        wolf.setheading(180)
        wolf.forward(step)

def go_left_dog(step):
    new_range = dog.xcor() - 15
    if (dog.distance(wolf.pos()) <= 85):
        dog.goto(wolf.pos())
        dog_on_wolf()
        turtle.mainloop()
    if new_range <= -x:
        go_right_dog(step)
    else:
        dog.setheading(180)
        dog.forward(step)

def go_left_sheep(step):
    new_range = sheep_leader.xcor() - 15
    if new_range <= -x:
        go_right_sheep(step)
    else:
        sheep_leader.setheading(180)
        sheep_leader.forward(step)

#Functions for "go down" for wolf, sheep, and dog
def go_down_wolf(step):
    new_range = wolf.ycor() - 15

    if (wolf.distance(sheep_leader.pos()) <= 85):
        wolf.goto(sheep_leader.pos())
        sheep_leader.hideturtle()
        turtle.mainloop()
    elif new_range <= -y:
        go_up_wolf(step)
    else:
        wolf.setheading(270)
        wolf.forward(step)

def go_down_dog(step):
    new_range = dog.ycor() - 15
    if (dog.distance(wolf.pos()) <= 85):
        dog.goto(wolf.pos())
        dog_on_wolf()
        turtle.mainloop()
    elif new_range <= -y:
        go_up_dog(step)
    else:
        dog.setheading(270)
        dog.forward(step)

def go_down_sheep(step):
    new_range = sheep_leader.ycor() - 15
    if new_range <= -y:
        go_up_sheep(step)
    else:
        sheep_leader.setheading(270)
        sheep_leader.forward(step)

#Function make_random_walk will use dictionaries to call the functions
def make_random_walk(step_size, step_number):
    move_dict_wolf = {1: go_up_wolf,
                      2: go_right_wolf,
                      3: go_left_wolf,
                      4: go_down_wolf
                      }
    move_dict_dog = {1: go_up_dog,
                     2: go_right_dog,
                     3: go_left_dog,
                     4: go_down_dog
                     }
    move_dict_sheep = {1: go_up_sheep,
                     2: go_right_sheep,
                     3: go_left_sheep,
                     4: go_down_sheep
                     }
    
    # Adds the images to the turtle objects for dog, sheep, and wolf, and assigns their position randomly within the 600x600 window
    wolf.hideturtle()
    screen.addshape(img_wolf)
    wolf.shape(img_wolf)
    wolf.setpos(random.randint(1,300),random.randint(1,300))
    wolf.showturtle()

    dog.hideturtle()
    screen.addshape(img_dog)
    dog.shape(img_dog)
    dog.setpos(random.randint(1, 300), random.randint(1, 300))
    dog.showturtle()

    sheep_leader.hideturtle()
    screen.addshape(img_sheep)
    sheep_leader.shape(img_sheep)
    sheep_leader.setpos(random.randint(1, 300), random.randint(1, 300))
    sheep_leader.showturtle()

#Will use the step_number parameter to declare range of iteration
    for _ in range(step_number):

        #These lines of code use random numbers from 1-4 to select and assign an item from the dictionary which will then call the function
        move_in_a_direction_turtle = move_dict_wolf[random.randint(1, 4)]
        move_in_a_direction_turtle(step_size)

        move_in_a_direction_dog = move_dict_dog[random.randint(1, 4)]
        move_in_a_direction_dog(step_size)

        move_in_a_direction_sheep = move_dict_sheep[random.randint(1, 4)]
        move_in_a_direction_sheep(step_size)

#This function will be called when the dog is in range of the wolf and attacks. The variables of strength for each animal (initialized below)
#will determine which animal succeeds in killing the other.
def dog_on_wolf():
    if dog_strength <= wolf_strength:
        dog.hideturtle()
    elif dog_strength > wolf_strength:
        wolf.hideturtle()

#These next few lines of code will import the python libraries for turtle and random.
import turtle
import random

#Draws the 600x600 border just for visual aesthetics
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

#These x and y variables are defined to be used later by the motion functions. They help make the comparisons for the objects so that 
#they don't fly off the 600x600 screen.
x = 300
y = 300

#These statements will assign a screen size of 600x600 to the desired window
screen = turtle.Screen()
screen.screensize(600, 600)

#Assigns the files of the three pictures to their respective variables
img_dog = r"C:\Users\andre\PycharmProjects\project\Dog.gif"
img_sheep = r"C:\Users\andre\PycharmProjects\project\LittleSheep.gif"
img_wolf = r"C:\Users\andre\PycharmProjects\project\wolf.gif"

#creates the three turtle objects, *(will need to create more sheep objects when working of reproduction)
dog = turtle.Turtle()
sheep_leader = turtle.Turtle()
wolf = turtle.Turtle()

#Picks up the pen so that a line is not drawn when the objects move
dog.penup()
sheep_leader.penup()
wolf.penup()

#Initializes the variables for step size (how large each movement will be) and step number (how many steps will be made)
step_size = 15
step_number = 1000

#Intializes the dog and wolf strength variable from a random number between 1-50
dog_strength = random.randint(1, 50)
wolf_strength = random.randint(1, 50)

#create_second_sheep()

make_random_walk(step_size, step_number)

turtle.mainloop()

#Now with the wolf, sheep, and dog all moving together, we will need to:
#   Spawn two additional sheep that stay near their initialized "leader".
#   Make sure that these additional sheep stay within a certain distance of their leader. If they reach that distance, they'll need
#   To be prompted to move closer to the leader

#   Create a "reproduction occurance" that happens whenever two sheep occupy the same space (or are within a certain distance of each other)
#       Initialize a respective variable "sheep_population" for comparison. Once the number of the sheep objects on the screen reaches that
#       number than the sheep win the round.

# Wolf on sheep interactions should just make the sheep invisible and should give the wolf some health
#   Must declare variables for wolf hunger and health
#       Initialize a variable "hunger" which will decrement with time. Once at zero the wolf will die.

#   Create a dictionary to keep track of which animal is winning




