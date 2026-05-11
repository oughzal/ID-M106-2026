from turtle import Turtle
from random import random
t = Turtle()
d = 0
n = 10
for i in range(100):
    t.forward(d)
    t.left(90)
    d += 1
    n += 1

t.screen.mainloop()