from turtle import *

shape('turtle')
speed('fastest')


def square(length=100):
    for i in range(4):
        forward(length)
        right(90)


def triangle(length=100):
    for i in range(3):
        forward(length)
        right(120)


def polygon(sides):
    for i in range(sides):
        forward(100)
        right(360/sides)


def circles_of_squares():
    for i in range(60):
        square()
        right(5)


def spiral(length=45):
    for i in range(60):
        length += 5
        square(length)
        right(5)

spiral()