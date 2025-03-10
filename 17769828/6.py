import turtle
from turtle import *
k = 10
tracer(0)
right(180)
forward(5 * k)
right(90)
forward(50 * k)
right(90)
forward(5 * k)
for i in range(5):
    circle(-5 * k, 180)
    left(180)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(4, 'red')
mainloop()