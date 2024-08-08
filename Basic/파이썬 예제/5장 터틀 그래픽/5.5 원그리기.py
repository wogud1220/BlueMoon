# 100개의 선분으로 원 그리기
import turtle

turtle.setup(width = 500, height = 500) 
edges = 100
length = 6
angle = 360 / edges
t = turtle.Turtle()
t.pencolor("blue")
t.width(5)
t.speed(6)
for i in range(edges):
    t.forward(length)
    t.right(angle)