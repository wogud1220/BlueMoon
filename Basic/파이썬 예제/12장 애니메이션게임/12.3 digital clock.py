from tkinter import * 
import time 
tk = Tk() 
canvas = Canvas(tk, width = 500, height = 500) 
canvas.pack() 
width = 500 
height = 500 
while 1: 
   t = time.localtime() 
   hour = t[3] 
   minute = t[4] 
   second = t[5]
   canvas.delete("all") 
   myclock = str(hour) + ":" + str(minute) + ":" + str(second)   
   canvas.create_text(250, 250, text = myclock) #, font=('Arial', 25)) 
   
   time.sleep(1)
   tk.update()
