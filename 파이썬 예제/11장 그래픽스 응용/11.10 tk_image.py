from tkinter import *
import random
import time

tk = Tk()
canvas = Canvas (tk, width=1000,height=1000)
canvas.pack()

image_list = ['Koala.gif','Penguins.gif']

while True:
    for img in image_list :
        myimage = PhotoImage(file=img)
        canvas.create_image(10,10, anchor = NW, image=myimage)
        tk.update()
        time.sleep(3)
