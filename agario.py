import turtle
import time
import random
import math
from ball import Ball
turtle.colormode(255) 
turtle.tracer(1)
turtle.hideturtle()
t=turtle.clone()
turtle.pu()
running=True
screen_width=turtle.getcanvas().winfo_width()/2
print(screen_width)
screen_height=turtle.getcanvas().winfo_height()/2
print(screen_height)
my_Ball=Ball(0,0,3,3,14,"pink")
number_of_Balls = 5
minimum_Ball_radius =10
maximum_Ball_radius = 50
minimum_Ball_dx = -5
maximum_Ball_dx = 5
minimum_Ball_dy = -5
maximum_Ball_dy = 5
Balls=[]
for i in range(number_of_Balls):
    print("mooving")
    y=random.randint((-screen_height + maximum_Ball_radius),(screen_height-maximum_Ball_radius))
    x=random.randint((-screen_width + maximum_Ball_radius) ,(screen_width-maximum_Ball_radius))
    Balldx=random.randint(minimum_Ball_dx,maximum_Ball_dx)
    Balldy=random.randint(minimum_Ball_dy,maximum_Ball_dy)
    Ballradius=random.randint(minimum_Ball_radius,maximum_Ball_radius)
    color=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    new_Ball=Ball(x,y,Balldx,Balldy,Ballradius,color)
    Balls.append(new_Ball)

def move_all_Balls():
    for x in Balls:
        x.move(screen_width,screen_height)

def colide(Ball1,Ball2):
    if Ball1 ==Ball2:
        return False
    d= math.sqrt(math.pow(Ball1.xcor() - Ball2.xcor(),2)+math.pow(Ball1.ycor() - Ball2.ycor(),2))
    if(d<=Ball1.r+Ball2.r):
        print('coliision')
        return True
    else:
        return False
def check_all_Balls_collision():
    all_Balls=[]
    all_Balls.append(my_Ball)
    for Ball in Balls:
        all_Balls.append(Ball)
    
    for Ball1 in all_Balls:
        for Ball2 in all_Balls:
            #colide(Ball1,Ball2)
            if(colide(Ball1,Ball2)==True):
                r1=Ball1.r
                r2=Ball2.r
                rand_x=random.randint(-screen_width + maximum_Ball_radius,screen_width - maximum_Ball_radius)
                rand_y=random.randint(-screen_height +maximum_Ball_radius,screen_height-maximum_Ball_radius)
                rand_dx=random.randint(minimum_Ball_dx,maximum_Ball_dx)
                rand_dy=random.randint(minimum_Ball_dy,maximum_Ball_dy)
                rand_r=random.randint(minimum_Ball_radius,maximum_Ball_radius)
                rand_color= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                #if my_Ball==Ball2 and r2<r1:
                 #   break
                #elif
                #my_Ball==Ball1 and r1<r2:   
                 #   break
                if r1>r2:
                    if Ball2 == my_Ball:
                        print("boom")
                      
                        turtle.goto(-300,-300)
                        turtle.color("black")
                        turtle.write("game over",font=("Comic Sans Ms",100,"normal"))
                        quit()
                    Ball2.new_Ball(rand_x,rand_y,rand_dx,rand_dy,rand_r,rand_color)
                    Ball1.r = Ball1.r + 10
                    Ball1.shapesize((Ball1.r )/10)
                    print('created')
                else:
                    if Ball1 == my_Ball:
                        print("boom")
                        
                        turtle.goto(-300,-320)
                        turtle.color("black")
                        turtle.write("game over",font=("Comic Sans Ms",100,"normal"))
                        quit()
                        
                    Ball1.new_Ball(rand_x,rand_y,rand_dx,rand_dy,rand_r,rand_color)
                    Ball2.r = Ball2.r + 10
                    print('created')
                    Ball2.shapesize((Ball2.r)/10) 

                    
def movearound():
    x = turtle.getcanvas().winfo_pointerx() - screen_width*2
    y = screen_height*2 - turtle.getcanvas().winfo_pointery()
    my_Ball.goto(turtle.getcanvas().winfo_pointerx() - screen_width*2, screen_height*2 - turtle.getcanvas().winfo_pointery())
while running==True:
    screen_width=turtle.getcanvas().winfo_width()/2
    screen_height=turtle.getcanvas().winfo_height()/2
    move_all_Balls()
    movearound()
    check_all_Balls_collision()
turtle.mainloop()
    

     
         

