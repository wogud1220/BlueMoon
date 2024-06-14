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

while 1:
    t = time.localtime()       

    second = t[5]*6

    sx = sr * math.sin(second/360 * 3.14*2)
    sy = sr * math.cos(second/360 * 3.14*2)

    canvas.delete("all")
     
    canvas.create_line(cx, cy, cx+sx, cy-sy, fill='Red', width = 2)
   
    time.sleep(1)
    tk.update()

