from turtle import *
k = 30
tracer(0)
pendown()
for i in range(8):
    right(45)
    forward(6*k)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*k, y*k)
        dot(4, 'red')
mainloop()