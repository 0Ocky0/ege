from turtle import *
tracer(0)
k = 20
for i in range(8):
    forward(16*k)
    right(90)
    forward(22*k)
    right(90)
penup()
forward(5*k)
right(90)
forward(5*k)
left(90)
pendown()
for i in range(8):
    forward(52*k)
    right(90)
    forward(77*k)
    right(90)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*k, y*k)
        dot(4, 'red')
mainloop()