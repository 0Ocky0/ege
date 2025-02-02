from turtle import *

tracer(0)
k = 15
for i in range(2):
    forward(k * 15)
    right(90)
    forward(8 * k)
    right(90)
left(90)
right(180)
forward(10.5*k)
right(180)
for i in range(2):
    forward(k * 15)
    right(90)
    forward(8 * k)
    right(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x * k, y * k)
        dot(4, 'red')
mainloop()
