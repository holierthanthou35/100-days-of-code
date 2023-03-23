from turtle import Turtle 
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.goto(x, y)