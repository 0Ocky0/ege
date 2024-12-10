from turtle import *
k = 30
tracer(0)
pendown()
for i in range(4):
    forward(12*k)
    right(90)
for i in range(5):
    forward(k*4)
    right(45)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*k, y*k)
        dot(4, 'red')
done()