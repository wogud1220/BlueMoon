# 삼각형을 그리고 내부를 칠하기

import turtle
t = turtle.Turtle() 
t.width(3) 
t.speed(5) 
t.color(1, 1, 0) 
t.pencolor(0, 0, 1) 
t.begin_fill() 
t.setheading(60) 
for i in range(3): 
   t.forward(100) 
   t.right(120) 
t.end_fill() 