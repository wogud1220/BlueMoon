from tkinter import *
import random
tk = Tk()
canvas = Canvas (tk, width=500,height=500)
canvas.pack()

for i in range(200):
    x1 = random.randrange(400)
    y1 = random.randrange(400)
    x2 = x1 + random.randrange(200)-100
    y2 = y1 + random.randrange(200)-100
    canvas.create_rectangle(x1, y1, x2, y2)
