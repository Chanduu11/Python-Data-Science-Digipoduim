from turtle import *
speed('fastest')

#polygon
distance=100
sides=6

for i in range(10):
  pencolor('red') # to change the color of pen
  fd(distance)
  rt(360/sides)
  circle(distance/2) # to draw the circle
  for i in range(sides):
    pencolor('green') #polygon inside a polygon
    fd(distance/2)
    rt(360/sides)
    dot(10)
    write(i)
    for i in range(sides):
      pencolor('blue')
      fd(distance/4)
      rt(360/sides)
 
hideturtle() # to hide the turtle
mainloop() # this line is to keep the window open