#from color import new_colors
import turtle as t
import random

i = 0
t.colormode(255)
k = t.Turtle()

k.penup()
k.setheading(225)
k.forward(300)
k.setheading(0)
k.hideturtle()
k.pencolor("white")
color_list = [(226, 229, 235), (244, 237, 222), (243, 234, 240), (232, 242, 237), (192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26), (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127)]


for _ in range(1, 101):

    k.dot(20, random.choice(color_list))
    k.fd(50)

    if _ % 10 == 0:

        k.setheading(90)
        k.forward(50)
        k.setheading(180)
        k.forward(500)
        k.setheading(0)




