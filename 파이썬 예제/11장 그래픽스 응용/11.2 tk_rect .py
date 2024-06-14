# 사각형 그리기
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
canvas.create_rectangle(100, 100, 400, 400)
