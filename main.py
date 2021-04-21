'''
03/22/2021
Introduction to Turtle

# 1. Import turtle library
import turtle

# 2. Create a pen/ turtle
variable1 = turtle.Turtle()

# 3. Create a paper/ screen
variable2 = turtle.Screen()

# 4. Movements
  a. move forward
    variable1.forward(DISTANCE)
    variable.fd(DISTANCE)
  b. Move backward
    variable1.backward(DISTANCE)
    variable1.bk(DISTANCE)
  c. turn right
    variable1.right(ANGLE)
  
  d. Turn left
    variable1.left(ANGLE)
  
  e. Pen up
    variable1.penup()
  f. Pen Down
    variable1.pendown()
  g. Go to Home(origin)
    variable1.home()
  h. Go to a specific point
    variable.goto(X,Y)  

import turtle

# Window
pen = turtle.Turtle() #Origin(0,0)
pen.fd(300)
pen.left(90)
pen.fd(200)
pen.left(90)
pen.fd(300)
pen.left(90)
pen.fd(400)
pen.left(90)
pen.fd(300)
pen.left(90)
pen.fd(400)
pen.left(90)
pen.fd(150)
pen.left(90)
pen.fd(407)

import turtle
#house
pen = turtle.Turtle()
pen.fd(100)
pen.left(90)
pen.fd(200)
pen.left(90)
pen.fd(200)
pen.right(150)
pen.fd(100)
pen.right(30)
pen.fd(50)
pen.right(30)
pen.fd(95)
pen.penup()
pen.home()
pen.pendown()
pen.left(90)
pen.fd(100)
pen.left(90)
pen.fd(50)
pen.left(90)
pen.fd(100)
pen.left(90)
pen.fd(50)
pen.bk(100)
pen.left(90)
pen.fd(200)


pen.penup()
pen.right(90)
pen.fd(50)
pen.right(90)
pen.fd(20)
pen.pendown()
pen.fd(50)
pen.left(90)
pen.fd(50)
pen.left(90)
pen.fd(50)
pen.left(90)
pen.fd(50)

pen.penup()
pen.home()
'''
color = "brown"
import turtle
#house
pen = turtle.Turtle()
pen.color(color)
pen.fd(100)
pen.left(90)
pen.fd(200)
pen.left(90)
pen.fd(200)
pen.right(150)
pen.fd(100)
pen.right(30)
pen.fd(50)
pen.right(40)
pen.fd(84)
pen.penup()
pen.home()
pen.pendown()
pen.left(90)
pen.fd(100)
pen.left(90)
pen.fd(50)
pen.left(90)
pen.fd(100)
pen.left(90)
pen.fd(50)
pen.bk(100)
pen.left(90)
pen.fd(200)

color = "blue"
pen.color(color)
pen.penup()
pen.right(90)
pen.fd(50)
pen.right(90)
pen.fd(20)
pen.pendown()
pen.fd(50)
pen.left(90)
pen.fd(50)
pen.left(90)
pen.fd(50)
pen.left(90)
pen.fd(50)

pen.penup()
pen.home()