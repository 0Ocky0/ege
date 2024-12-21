from turtle import *
k = 30
tracer(0)
pendown()
for i in range(12):
    right(60)
    forward(k*1)
    right(60)
    forward(k * 1)
    right(270)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*k, y*k)
        dot(4, 'red')
mainloop()