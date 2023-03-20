import turtle as t

k = t.Turtle()
screen = t.Screen()

def forward():
    k.forward(30)

def backward():
    k.back(30)

def clockwise():
    k.right(30)

def anticlockwise():
    k.left(30)

def clear():
    k.reset()

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=anticlockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)


screen.exitonclick()