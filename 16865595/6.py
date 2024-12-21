from turtle import *
k = 20
tracer(0)
right(270)
pendown()
for i in range(2):
    forward(24 * k)
    right(90)
    forward(10*k)
    right(90)
forward(3*k)
left(90)
forward(13*k)
right(90)
for i in range(2):
    forward(9 * k)
    right(90)
    forward(32*k)
    right(90)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*k, y*k)
        dot(4, 'red')
done()