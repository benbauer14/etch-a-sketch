from turtle import Turtle, Screen

ben = Turtle()
screen = Screen()

def moveLeft():
    ben.left(15)

def moveRight():
    ben.right(15)

def moveForward():
    ben.forward(10)


screen.onkeypress(fun=moveLeft,key="Left")
screen.onkeypress(fun=moveRight,key="Right")
screen.onkeypress(fun=moveForward,key="Up")
screen.listen()

screen.exitonclick()