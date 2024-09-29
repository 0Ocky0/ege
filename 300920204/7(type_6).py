from turtle import *
k = 30
tracer(0)
pendown()
for i in range(3):
    forward(7*k)
    right(90)
forward(8*k)
for i in range(3):
    left(90)
    forward(5*k)
penup()
for x in range(-50, 50):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot(4, 'red')
done()