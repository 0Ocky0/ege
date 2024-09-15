from turtle import *
k = 50
tracer(0)
pendown()
for i in range (12):
    right(60)
    forward(1 * k)
    right(60)
    forward(1 * k)
    right(270)
penup()
for x in range(-50, 50):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot(4, 'red')
done()