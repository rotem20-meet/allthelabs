#ex1-3
for i in range(100):
 print("rotem")
num=5 
print(num)
num1=num/2
print(num1)
list_numbers=[2,4,7]
total=0
for i in range(0,3):
    print(list_numbers[i])
    total=total+list_numbers[i]
    print(total)
#ex4
import turtle
import random
turtle.colormode(255)
turtle.begin_fill()
for i in range(5):
    r=random.randint(1,200)
    b=random.randint(1,200)
    g=random.randint(1,200)
    turtle.color(r,g,b)
    turtle.begin_fill()
    turtle.penup()
    turtle.circle(100)
    turtle.end_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
