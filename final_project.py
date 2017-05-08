#Define master class of Animal
import turtle
import random

#Defines the super class Animal with properties of image, and x, y coordinates
class Animal:
    def __init__(self, image = "filepath", x = 0, y = 0):
        self.image = image
        self.turtle = turtle.Turtle()
        self.x = x
        self.y = y

        self.boundx = 300
        self.boundy = 300

        self.turtle.hideturtle()

        #Adds the objects image to the screen
        if image != "none":
            screen.addshape(self.image)
            self.turtle.shape(self.image)

        #Picks up the turtle pen and sets the postions to the passed in parameters. Shows the image.
        self.turtle.penup()
        self.turtle.setpos(x, y)
        self.turtle.showturtle()

    def check_x_cor(self, x):
        if x > 300:
            return 300
        elif x < -300:
            return -300
        else:
            return x

    def check_y_cor(self, y):
        if y > 300:
            return 300
        elif y < - 300:
            return -300
        else:
            return y

    #Defines the function for rightward movement of the objects
    #Stays within the bounds of the 300 by 300 square
    def go_right(self, step):
        new_range = self.turtle.xcor() + 15
        if new_range >= self.boundx:
            self.go_left(step)
        else:
            self.turtle.setheading(0)
            self.turtle.forward(step)

    #Defines the function for the upward movement of the objects
    #Stays within the bounds of the 300 by 300 square
    def go_up(self, step):
        new_range = self.turtle.ycor() + 15
        if new_range >= self.boundy:
            edge = new_range - self.boundy
            new_step = step - edge
        else:
            new_step = step

        self.turtle.setheading(90)
        self.turtle.forward(new_step)

    #Defines the function for the leftward movement of the objects
    #Stays within the bounds of the 300 by 300 square
    def go_left(self, step):
        new_range = self.turtle.xcor() - 15
        if new_range <= -self.boundx:
            self.go_right(step)
        else:
            self.turtle.setheading(180)
            self.turtle.forward(step)

    #Defines the function for the downward movement of the objects
    #Stays within the bounds of the 300 by 300 square
    def go_down(self, step):
        new_range = self.turtle.ycor() - 15
        if new_range <= -self.boundy:
            self.go_up(step)
        else:
            self.turtle.setheading(270)
            self.turtle.forward(step)

    #When called, uses the dictionary and step size to drive the other four movement functions above
    def make_random_walk(self, step_size):
        move_dict = {1: self.go_up,
                     2: self.go_right,
                     3: self.go_left,
                     4: self.go_down
                     }

        move_in_a_direction = move_dict[random.randint(1, 4)]
        move_in_a_direction(step_size)

#Defines the Sheep subclass of the Animal super class
#Possesses the properties of image, and x and y coordinates
#Contains the "move" function which contains the x and y coordinates of the flock (Passed through)
class Sheep(Animal):
    def __init__(self, image = "filepath", x = 0, y = 0):
        super().__init__(image, x, y)

    #Contains an IF statement which, if the sheep move 125 pixels away from the flock, a "goto" statement is used to guide the sheep object
    #back to the flock
    def move(self, flockx = 0, flocky = 0):
        if (self.turtle.distance(flockx, flocky) >= 125):
            self.turtle.goto(flockx, flocky)
        else:
            self.make_random_walk(15)

class Wolf(Animal):
    def __init__(self, image = "unknown", x = 0, y = 0):
        super().__init__(image, x, y)
        self.strength = random.randint(1, 50)

    def move(self, sheep):
        for i in range(len(sheep)):
            if self.turtle.distance(sheep[i].turtle.pos()) <=125:
                self.turtle.goto(sheep[i].turtle.pos())
                sheep[i].turtle.hideturtle()
                del sheep[i]
                return True
        self.make_random_walk(15)

#Defines the Dog subclass of the Animal super class
#Initializes with the properties image, and x and y coordinates
#Inherents the image and coordinates from the super class
#Randomizes the Dog's strength variable from 1-50
#Contains the "move" and "dog_on_wolf" functions
class Dog(Animal):
    def __init__(self, image = "unknown", x = 0, y = 0):
        super().__init__(image, x, y)
        self.strength = random.randint(1, 50)

    #Contains an IF statement that tells the Dog to attack the Wolf if the distance between the two objects (85 pixels)
    #Returns the boolean value of the dog_on_wolf() function
    def move(self, wolf, flock):
        if self.turtle.distance(wolf.turtle.pos()) <= 125:
            self.turtle.goto(wolf.turtle.pos())
            return self.dog_on_wolf(wolf)

        #Acts like the Sheep in that the Dog stays within 250 pixels of the Flock cursor
        if (self.turtle.distance(flock.turtle.xcor(), flock.turtle.ycor()) >= 250):
            self.turtle.goto(flock.turtle.xcor(), flock.turtle.ycor())
        else:
            self.make_random_walk(15)

    #If the Dog is weaker than the Wolf, the Dog disapears and the Wolf is free to kill the sheep (Returns False)
    #If the Dog is stronger than the Wolf, the Wolf disapears and the function returns True
    def dog_on_wolf(self, wolf):
        if self.strength < wolf.strength:
            self.turtle.hideturtle()
            return False

        elif self.strength > wolf.strength:
            wolf.turtle.hideturtle()
            total_scores["Dog"] += 1
            return True

#Sub class Flock that inherits from the super class Animal
#Possesses qualities of image and x and y coordinates
class Flock(Animal):
    def __init__(self, image = "none", x = 0, y = 0):
        #Inherits the image and coordinates
        super().__init__(image, x, y)

        self.turtle.hideturtle()

        #Initializes a list which will contain the sheep objects
        self.sheep_list = []

        #Initializes the original three sheep images (Using 0-7 notation for indexing)
        self.img_sheep0 = r"C:\Users\andre\PycharmProjects\project\LittleSheep0.gif"
        self.img_sheep1 = r"C:\Users\andre\PycharmProjects\project\LittleSheep1.gif"
        self.img_sheep2 = r"C:\Users\andre\PycharmProjects\project\LittleSheep2.gif"

        #Creates the three Sheep objects and appends them to the list
        self.sheep_list.append(Sheep(self.img_sheep0, x, y))
        self.sheep_list.append(Sheep(self.img_sheep1, self.check_x_cor(random.randint((x - 75), (x + 75))), self.check_y_cor(random.randint((y - 75), (y + 75)))))
        self.sheep_list.append(Sheep(self.img_sheep2, self.check_x_cor(random.randint((x - 75), (x + 75))), self.check_y_cor(random.randint((y - 75), (y + 75)))))

        #Initializes counters to keep track of how many sheep have reproduced, and how many images are being used (From 0, 1, 2)
        self.reproduction_counter = 0
        self.img_counter = 2

    #Returns the sheep list for the Wolf object to reference
    def get_sheep(self):
        return self.sheep_list

    def remove_sheep(self):
        for i in range(len(self.sheep_list)):
            self.sheep_list[i].turtle.hideturtle()

    #Function checks to see if two seperate Sheep objects occupy a space less than or equal to 20 pixels
    #Uses a double for loop to iterate through the Sheep objects and make comparisons
    #If the objects do not reference the same object then the reproduction_counter is incremented
    #Once the reproduction_counter hits a total of twenty interactions, only then will the "reproduction()" function be called
    def check_reproduction(self):
        for i in range(len(self.sheep_list)):
            for j in range(len(self.sheep_list)):
                if (i != j) and (self.sheep_list[i].turtle.distance(self.sheep_list[j].turtle.pos()) <= 20):
                    self.reproduction_counter += 1
                    if self.reproduction_counter == 10:
                        self.reproduction()
                        self.reproduction_counter = 0

    #Once called the function will increment the img_counter
    #Then a new image directory will be created through string concatination
    #This link will be used when creating a new Sheep object to later be appended to the sheep_list
    def reproduction(self):
        self.img_counter += 1
        image_reproduction = r"C:\Users\andre\PycharmProjects\project\LittleSheep" + str(self.img_counter) + ".gif"
        self.sheep_list.append(Sheep(image_reproduction, self.check_x_cor(random.randint((self.x - 75), (self.x + 75))), self.check_y_cor(random.randint((self.y - 75), (self.y + 75)))))

    #Moves all of the existing sheep objects
    #After movement the comparison is made using the check_reproduction() function
    def move(self):
        self.make_random_walk(15)

        for i in range(len(self.sheep_list)):
            self.sheep_list[i].move(self.turtle.xcor(), self.turtle.ycor())

        self.check_reproduction()

# Drives the objects motion
# The flock operates independant of paramaters
# The wolf operates with the parameter of the "get_sheep" list containing the sheep objects
# The dog operates with the parameters of the wolf and flock objects
def drive_simulation():
    # Draws the boundaries for the objects to operate on
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

    # Assigns the wolf and dog images to be used in the instantiation
    img_wolf = r"C:\Users\andre\PycharmProjects\project\wolf.gif"
    img_dog = r"C:\Users\andre\PycharmProjects\project\Dog.gif"

    # Creates and initializes the postions and qualities of the animal objects
    flock = Flock("none", random.randint(-300, 300), random.randint(-300, 300))
    wolf = Wolf(img_wolf, random.randint(-300, 300), random.randint(-300, 300))
    dog = Dog(img_dog, flock.turtle.xcor(), flock.turtle.ycor())

    for i in range(1500):
        flock.move()
        wolf.move(flock.get_sheep())
        if dog.move(wolf, flock):
            break

        if len(flock.sheep_list) == 8:
            total_scores["Sheep"] += 1
            break
        elif len(flock.sheep_list) == 0:
            total_scores["Wolf"] += 1
            break
    print(total_scores)


    flock.remove_sheep()
    turtle.clear()

#__main__
# Creates a dictionary "total scores" that containes the total number of wins for each animal object
total_scores = {"Dog": 0, "Sheep": 0, "Wolf": 0}

#screen = None

# Creates the screen
screen = turtle.Screen()
screen.screensize(600, 600)

response = "yes"
while response == "yes":
    drive_simulation()
        #response = str(input("Do you want to run the simulation? (yes/no)"))
turtle.mainloop()
