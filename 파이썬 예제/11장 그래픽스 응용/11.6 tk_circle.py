from tkinter import *
import random
import time

tk = Tk()
canvas = Canvas (tk, width=500,height=500)
canvas.pack()
width = 500
height = 500
step = 5

for i in range(10, 250, step):
    x1 = width/2-i
    y1 = height/2-i
    x2 = width/2+i
    y2 = height/2+i
    canvas.create_arc(x1, y1, x2, y2, extent = 359, style = ARC)
    tk.update()
    time.sleep(0.05)
  
