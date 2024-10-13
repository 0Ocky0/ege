from turtle import *
k = 60
tracer(0)
pendown()
for i in range (4):
    forward(8*k)
    right(90)
for i in range(3):
    forward(12*k)
    right(120)
penup()
for x in range(-50, 50):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(4, 'red')
done()
