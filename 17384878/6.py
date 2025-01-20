from turtle import *

tracer(0)
k = 30
for i in range(4):
    forward(7 * k)
    right(90)
    forward(8 * k)
    right(90)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x * k, y * k)
        dot(4, 'red')
mainloop()