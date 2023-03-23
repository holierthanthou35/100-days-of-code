import turtle as t
from snake2 import Snake
import time
from food import Food
from scoreboard import Scoreboard

game_is_on = True
t.bgcolor("black")
screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("snake game")
all_body = []
screen.tracer(0)

snake = Snake()
food_ = Food()
scores = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food_) < 10:
        food_.refresh()
        scores.score_counter()

screen.exitonclick()
