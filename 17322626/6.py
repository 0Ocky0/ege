from turtle import *

tracer(0)
k = 20
left(90)
for i in range(2):
    forward(20 * k)
    right(90)
    forward(9 * k)
    right(90)
penup()
right(180)
for i in range(2):
    forward(20 * k)
    left(90)
    forward(9 * k)
    left(90)
right(180)
right(90)
pendown()
for i in range(2):
    forward(20 * k)
    left(90)
    forward(9 * k)
    left(90)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x * k, y * k)
        dot(4, 'red')
mainloop()
