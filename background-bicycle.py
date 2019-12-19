# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 23:11:43 2019

@author: Nicolas
"""

import turtle as tu
from turtle import Screen


def hexagon(dim_cote, color_hex):
    tu.color(color_hex)
    for i in range(6):
        for j in range(3):
            tu.fd(dim_cote)
            tu.lt(360/3)
        tu.lt(60)

def triangle(dim_cote, color_tri):
    tu.color(color_tri)
    for i in range(3):
        tu.fd(dim_cote)
        tu.lt(360/3)
        
def tree_branch():
    tu.lt(80)
    tu.fd(25)
    tu.color('green')
    tu.fd(35)
    hexagon(35, 'green')
    tu.penup()
    tu.bk(60)
    tu.color('brown')
    tu.pendown()
    tu.rt(80)

# initialization (set position to left)
tu.penup()
tu.setx(-300)
tu.pendown()
tu.color('grey')
tu.fd(600)

## bicycle
# first wheel
tu.setx(-200)
tu.penup()
tu.lt(90)
tu.fd(20)
tu.pendown()
tu.color('yellow')
hexagon(20, 'yellow')

# bicycle body
tu.rt(30)
tu.color('orange')
tu.fd(50)
tu.rt(120)
triangle(50, 'orange')
tu.lt(105)
tu.color('red')
tu.fd(20)
tu.bk(20)
tu.color('orange')
tu.rt(45)
tu.fd(50)
tu.rt(120)
triangle(50, 'orange')
tu.lt(165)
tu.color('red')
tu.fd(20)
tu.lt(135)
tu.fd(15)

# second wheel
tu.bk(15)
tu.lt(45)
tu.fd(20)
tu.color('orange')
tu.lt(75)
tu.fd(50)
tu.lt(30)
hexagon(20, 'yellow')

# tree
tu.penup()
tu.home()
tu.setx(100)
tu.pendown()
tu.lt(90)
tu.color('brown')
tu.fd(50)
tree_branch()
tu.fd(70)
tree_branch()
tu.fd(50)
tu.color('green')
tu.fd(60)
hexagon(60, 'green')



tu.hideturtle()
tu.done()