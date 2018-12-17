import turtle
turtle.register_shape("trash.gif")
turtle.shape('trash.gif')
turtle.speed(0)
turtle.pensize(1)
colors=['blue',"red","pink","green","yellow","purple"]
for i in range(360):
    turtle.pencolor(colors[i%6])
    turtle.fd(200)
    turtle.right(45)
    turtle.fd(100)
    turtle.left(90)
    turtle.home()
    turtle.right(i)
    
