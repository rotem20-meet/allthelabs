from turtle import *
import random
import math
class ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius=radius
        self.color(color)
        self.speed(speed)
ball1=ball(10,"green",10)
ball2=ball(2,"black",3)
def check(ball,ball2):
    if ball.radius+ball2.radius>= math.sqrt(math.pow((ball.xcor()-ball2.xcor()),2)+math.pow((ball.ycor()-ball2.ycor()),2)):
        print("good")
    else:
        print("not good")
def checklist(listt):
    for j in range(len(listt)-1):
        if listt[j].radius+listt[j+1].radius>= math.sqrt(math.pow((listt[j].xcor()-listt[j+1].xcor()),2)+math.pow((listt[j].ycor()-listt[j+1].ycor()),2)):
            print("good")
        else:
            print("not good")
        print("did the " +str(j) +"and"+str(j+1))
        j=j+1
  
#ball1.goto(100,100)
#check(ball1,ball2)
listofballs=[ball1,ball2]
checklist(listofballs)
