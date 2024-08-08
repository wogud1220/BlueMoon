from tkinter import *
import time
import math

tk = Tk()
canvas = Canvas (tk, width=500,height=500)

canvas.pack()

width = 500
height = 500
cx = width/2
cy = height/2
sr = height /2 - 50
mr = height /2 - 80
hr = height /2 - 110

while 1:
    t = time.localtime()       
    
    hour = (t[3] + t[4]/60) * 30
    minute = (t[4] + t[5]/60)* 6
    second = t[5]*6

    canvas.delete("all")
    
    hx = hr * math.sin(hour/360 * 3.14*2)
    hy = hr * math.cos(hour/360 * 3.14*2)
    canvas.create_line(cx, cy, cx+hx, cy-hy, fill='Blue', width = 10)
    
    mx = mr * math.sin(minute/360 * 3.14*2)
    my = mr * math.cos(minute/360 * 3.14*2)
    canvas.create_line(cx, cy, cx+mx, cy-my, fill='Green', width = 6)
    
    sx = sr * math.sin(second/360 * 3.14*2)
    sy = sr * math.cos(second/360 * 3.14*2)
    canvas.create_line(cx, cy, cx+sx, cy-sy, fill='Red', width = 2)
    tk.update()    
    time.sleep(1)


