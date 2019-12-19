import turtle as tu
from turtle import Screen

bob = tu.Turtle()

def drawEquiTriangle(tu, dist, colorTriangle):
    tu.pencolor(colorTriangle)
    for i in range(3):
        tu.fd(dist)
        tu.lt(360/3)
    tu.pencolor("black")
    tu.penup()
    tu.home()
    tu.pendown()

def drawSquare(tu, dist, colorSquare):
    tu.pencolor(colorSquare)
    for i in range(4):
        tu.fd(dist)
        tu.lt(360/4)
    tu.pencolor("black")
    tu.penup()
    tu.home()
    tu.pendown()

def drawHouse(tu):
    tu.penup()
    tu.fd(20)
    tu.pendown()
    drawSquare(bob, 40, "red")
    tu.penup()
    tu.lt(90)
    tu.fd(80)
    tu.rt(90)
    tu.pendown()
    drawEquiTriangle(bob, 80, "green")
    drawSquare(bob, 80, "black")
    tu.fd(20)
    
    tu.home()
    


drawHouse(bob)



bob.screen.exitonclick()