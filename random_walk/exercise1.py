import turtle
import random


def random_walk(n):
    turtle.setposition(0,0)
    for i in range(n):
        turtle.setheading(random.random()*360)
        turtle.forward(10)

    return turtle.position()

n = int(raw_input("How many steps would you like to random walk? "))

random_walk(n)

print "The turtle is at ",
print turtle.position()

turtle.exitonclick()
