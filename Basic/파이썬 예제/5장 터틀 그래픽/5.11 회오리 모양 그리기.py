# 반복적으로 움직이는 길이를 늘여나가며 그리는 회오리 모양
 
import turtle 
t= turtle.Turtle() 
t.color('blue') 
t.speed(0) 
angle = 91 
for x in range(200): 
    t.forward(x) 
    t.left(angle) 
t.hideturtle()