from turtle import *

k = 30
tracer(0)
for i in range(5):
    forward(9 * k)
    right(90)
    forward(3*k)
    right(90)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(4, 'red')
mainloop()