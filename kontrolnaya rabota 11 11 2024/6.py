from turtle import *
k = 30
tracer(0)
pendown()
for i in range(6):
    forward(13 * k)
    right(120)
penup()
for x in range(-50, 50):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(4, 'red')
done()
