import turtle
import random

turtle.circle(20)
turtle.speed(0)

answer = ''

while answer.lower() != 'n':
    answer = turtle.textinput("нарисовать окружность?", "Y/N")
    if answer.lower() == 'y':
        turtle.penup()
        turtle.goto(random.randrange(-300,300), random.randrange(1,100))
        turtle.pendown()
        turtle.circle(random.randrange(1,100))
    else:
        pass

