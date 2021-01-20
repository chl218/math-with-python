from turtle import *

shape('turtle')
speed('fastest')


def square(side_len=100):
    for i in range(4):
        forward(side_len)
        right(90)


def triangle(side_len=100):
    for i in range(3):
        forward(side_len)
        right(120)


def polygon(sides):
    for i in range(sides):
        forward(100)
        right(360/sides)


def circles_of_squares():
    for i in range(60):
        square()
        right(5)


input()
