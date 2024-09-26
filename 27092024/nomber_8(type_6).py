from turtle import *
k = 30
tracer(0)
left(270)
pendown()
for i in range(6):
    forward(10*k)
    right(60)
penup()
for x in range(-50, 50):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot(4, 'red')
done()