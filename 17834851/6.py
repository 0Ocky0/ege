from turtle import *

tracer(0)
k = 10
for i in range(9):
    forward(22 * k)
    right(90)
    forward(6*k)
    right(90)
penup()
forward(k)
right(90)
forward(5*k)
left(90)
pendown()
for i in range(9):
    forward(53 * k)
    right(90)
    forward(75*k)
    right(90)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(4, 'red')
mainloop()