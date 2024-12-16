from turtle import *
k = 20
tracer(0)
pendown()
for i in range(5):
    seth(90)
    circle(5 * k, 180)
    penup()
for x in range(0, 20):
    for y in range(0, 20):
        setpos(x * k, y * k)
        dot(5, 'red')
mainloop()
