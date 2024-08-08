# 원을 그리고 칠하기

import turtle 
import random 

turtle.setup(width = 500, height = 500) 
t = turtle.Turtle() 
t.width(3) 
t.speed(5) 
t.color(1, 1, 0) 
t.pencolor(0, 0, 1) 
t.begin_fill() 
t.circle(50)  
t.end_fill() 