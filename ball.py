from turtle import *
class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.pu()
        self.shape("circle")
        self.shapesize(r/10)
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color(color)
    def move(self,screen_width,screen_height):
        current_x=self.xcor()
        new_x=current_x+self.dx
        current_y=self.ycor()
        new_y=current_y+self.dy
        right_side_Ball=new_x+self.r
        upper_side_Ball=new_y+self.r
        left_side_Ball=new_x-self.r
        lower_side_Ball=new_y-self.r
        self.goto(new_x,new_y)
        if screen_width<=right_side_Ball or -screen_width>=left_side_Ball: 
            self.dx=(self.dx)*-1
        if screen_height<=upper_side_Ball or -screen_height>=lower_side_Ball:
            self.dy=self.dy*-1
                           
    def new_Ball(self,x,y,dx,dy,r,color):
        self.pu()
        self.shape("circle")
        self.shapesize(r/10)
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color(color)
