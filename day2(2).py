import turtle as t
import random

the_race = False
screen = t.Screen()
screen.setup(width= 600, height=400)
colors = ["Red", "Yellow", "Blue","Orange", "Green", "Violet"]
user_bet = screen.textinput(title="what is your bet?", prompt="enter the color")
all_turtles = []


for turtle_index in range(0,5):
    turtle = t.Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-270, y= (-180) + (turtle_index * 60))
    all_turtles.append(turtle)

if user_bet:
    the_race = True

while the_race:

    for turtle in all_turtles:
        rand_dist = random.randint(1,20)
        turtle.forward(rand_dist)

        if turtle.xcor() >= 280:
            the_race = False
            winner = turtle.pencolor()
            print(winner)

            if winner != user_bet:
                print("you lost!")

            else:
                print("you won!!")


screen.exitonclick() 