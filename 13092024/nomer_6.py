from turtle import *
k = 30
tracer(0)
pendown()
right(45)
for i in range (7):
    forward(5 * k)
    right(45)
    forward(10 * k)
    right(135)
penup()
for x in range(-50, 50):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot(4, 'red')
done()