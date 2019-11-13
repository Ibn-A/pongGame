# Simple pong in Python 3 for Beginners
# By @IbnA
# Part 1: Getting Started

import turtle

wn = turtle.Screen()
wn.title("Pong by @IbnA")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)




#Main game loop
while True:
    wn.update()
