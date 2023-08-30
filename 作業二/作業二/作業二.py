import random
import turtle
n=random.randint(50,100)
turtle.mode("standard")
turtle.forward(n)
for i in range(3):
    turtle.left(120)
    turtle.forward(100)
for j in range(2):
    turtle.left(240)
    turtle.forward(100)
