from turtle import *

k = 30
tracer(0)
right(90)
for i in range(4):
    forward(4 * (5 ** 0.5) * k)
    right(150)
    forward(4 * (5 ** 0.5) * k)
    right(300)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x * k, y * k)
        dot(4, 'red')
mainloop()
