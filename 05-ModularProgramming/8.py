import turtle 
def drawSquare(x,y,n):
    turtle.setpos(x,y)
    for i in range(4):
        turtle.forward(n)
        turtle.right(90)
def kwadrat():
    for i in range(4):
        turtle.forward(85)
        turtle.right(90)
def rysunek():
    for n in range(4):
        kwadrat()
        turtle.penup()
        turtle.forward(85)
        turtle.down()
    for n in range(3):
        turtle.right(180)
        turtle.penup()
        turtle.forward(4*85)
        turtle.right(270)
        turtle.forward(85)
        turtle.down()
        turtle.right(270)
        for n in range(4):
            kwadrat()
            turtle.penup()
            turtle.forward(85)
            turtle.down()
    
        
    
    
    
        
