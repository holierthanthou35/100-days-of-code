import turtle as t

class Snake:

    def __init__(self):
        self.all_body = []
        self.create_snake()
        self.head = self.all_body[0]

    def create_snake(self):
        for _ in range(0,3):

                k = t.Turtle("square")
                k.penup()
                k.color("white")
                k.goto(x=0-(_*20), y=0 )
                self.all_body.append(k)

    def move(self):
        for part_num in range(len(self.all_body) - 1, 0, -1):
            new_x = self.all_body[part_num - 1].xcor()
            new_y = self.all_body[part_num - 1].ycor()
            self.all_body[part_num].goto(new_x, new_y)
        self.head.forward(10)
        
    def up(self):
         if self.head.heading() != 270:
             self.head.setheading(90)

    def down(self):
         if self.head.heading() != 90:
             self.head.setheading(270)

    def right(self):
         if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
         if self.head.heading() != 0:
            self.head.setheading(180)