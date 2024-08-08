# 오각형이 그려지는 속도를 조절한다

import turtle
turtle.setup(width = 600, height = 600)
t = turtle.Turtle()
t.width(10)
t.pencolor("pink")

for i in [1, 3, 6, 10, 0]:
    t.speed(i)
    t.forward(150)
    t.right(72)
t.pencolor("red")
for i in ['slowest', 'slow', 'normal', 'fast', 'fastest']:
    t.speed(i)
    t.forward(150)
    t.right(72)
