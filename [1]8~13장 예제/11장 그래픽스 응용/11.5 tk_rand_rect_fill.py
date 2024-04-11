# 무작위로 사각형을 그리고 칠하기
from tkinter import *
import random
import time

tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
colors = ['red','pink','blue','purple','violet','orange','yellow', 'green']
for i in range(200):
    x1 = random.randrange(400)
    y1 = random.randrange(400)
    x2 = x1 + random.randrange(200) - 100
    y2 = y1 + random.randrange(200) - 100
    canvas.create_rectangle(x1, y1, x2, y2, fill = random.choice(colors))
    tk.update()
    time.sleep(0.05)
