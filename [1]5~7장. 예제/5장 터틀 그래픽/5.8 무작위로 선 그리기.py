# 무작위로 선을 그리기
import turtle 
import random 

turtle.setup(width = 500, height = 500) 
t = turtle.Turtle() 
t.width(3) 
t.speed(5) 
for i in range(200):  
  t.pencolor(random.random(), random.random(), random.random())
  length = random.randint(10, 60) 
  angle = random.randint(30, 120) 
  t.forward(length) 
  t.right(angle)