import turtle
from turtle import *
import random
turtle.colormode(255)
class Hexagon(Turtle):
    def __init__(self,size,color,speed):
        Turtle.__init__(self)
        self.size = size
        self.color=color
        self.speed=speed

    def random_color(self):
        r = random.randint(0,256)
        g = random.randint(0,256)
        b = random.randint(0,256)
        self.color= color(r,g,b)
    def my_shape(self):
        self.begin_poly()
        self.home()
        self.fd(100)
        self.left(60)
        self.fd(100)
        self.left(60)
        self.fd(100)
        self.left(60)
        self.fd(100)
        self.left(60)
        self.fd(100)
        self.left(60)
        self.fd(100)
        self.left(60)
        self.end_poly()
        p = self.get_poly()
        register_shape("hexagon",p)
        self.shape("hexagon")
    def change_speed(self):
        self.speed=random.randint(1,100)
        
s=Hexagon(10,"black",10)
s.random_color()
s.my_shape()
s.change_speed()
