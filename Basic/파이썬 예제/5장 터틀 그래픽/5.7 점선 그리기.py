# up과 down으로 점선 그리기

import turtle 
turtle.setup(width = 500, height = 500) 
t = turtle.Turtle() 
t.pencolor("dark green") 
t.width(3)
edges = 4
dot_size = 25

for i in range(edges): 
   for j in range(edges):   
      t.forward(dot_size) 
      t.up()
      t.forward(dot_size) 
      t.down()
   t.right(90) 