import turtle as t
import random
import time
from paddles import Paddles
from ball import Ball

game_is_on = True
k = t.Turtle()
k.color("white")
k.penup()
screen = t.Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("PING PONG")
score_l = 0
score_r = 0
#k.setposition(350, 40)

r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
ball_ = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball_.move()
    ball_.collision_y_wall()

    if (ball_.distance(r_paddle) < 50 or ball_.distance(l_paddle) < 50) and (ball_.xcor() > 340 or ball_.xcor() < -340):
        ball_.collision_paddle()
    
    if ball_.xcor() > 380:
        ball_.goto(0,0)
        score_l += 1
        ball_.collision_paddle()

    if ball_.xcor() < -380:
        ball_.goto(0,0)
        score_r += 1
        ball_.collision_paddle()

    k.goto(0, 270)
    k.clear()
    k.write(f"Score:{score_l} : {score_r}", align='center', font=('Arial', 24, 'normal'))

screen.exitonclick()