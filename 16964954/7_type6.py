from turtle import *
k = 30
tracer(0)
forward(-10 * k)
left(90)
pendown()
for i in range(4):
    forward(14 * k)
    right(90)
for i in range(5):
    forward(5 * k)
    right(45)
penup()
for x in range(-50, 50):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot(4, 'red')
done()