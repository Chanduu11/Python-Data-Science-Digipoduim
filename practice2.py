from turtle import *
speed('fastest')

#star
sides=10
distance=80
for i in range(sides):
    pencolor('yellow')
    rt(144)
    fd(distance)
    lt(72)
    fd(distance)
    pencolor('blue')
    circle(distance/4)
    for i in range(sides):
      pencolor('red')
      rt(144)
      fd(distance/2)
      lt(72)
      fd(distance/2)
      dot(10)
      write(i)
      pencolor('pink')
      circle(distance/4)

 
 
hideturtle() # to hide the turtle
mainloop()