from tkinter import *
import time
import math

tk = Tk()
canvas = Canvas (tk, width=500,height=500)
canvas.configure(background='white')
canvas.pack()
width = 500
height = 500
cx = width/2
cy = height/2
sr = height /2 - 50
mr = height /2 - 80
hr = height /2 - 110

def draw_label():
    for angle in range(30, 390, 30):    
        dr1 = height /2 - 25    # for unit line start
        dx1 = dr1 * math.sin(angle/360 * 3.14*2)
        dy1 = dr1 * math.cos(angle/360 * 3.14*2)

        dr2 = height /2 - 10    # for unit line end
        dx2 = dr2 * math.sin(angle/360 * 3.14*2)
        dy2 = dr2* math.cos(angle/360 * 3.14*2)

        dr3 = height /2 - 40    # for unit text
        dx3 = dr3 * math.sin(angle/360 * 3.14*2)
        dy3 = dr3 * math.cos(angle/360 * 3.14*2)

        canvas.create_line(cx+dx1, cy-dy1, cx+dx2, cy-dy2, fill='Black', width = 2)
        canvas.create_text(cx+dx3, cy-dy3, text=str(int(angle/30)), font=('Arial', 12))


while 1:
    t = time.localtime()       
    
    hour = (t[3] + t[4]/60)* 30
    minute = (t[4] + t[5]/60)*6
    second = t[5]*6

    canvas.delete("all")
    canvas.create_arc(10,10,width-10,height-10, extent=359,style=CHORD, width = 2)
    
    draw_label()
    hx = hr * math.sin(hour/360 * 3.14*2)
    hy = hr * math.cos(hour/360 * 3.14*2)

    canvas.create_line(cx, cy, cx+hx, cy-hy, fill='Blue', width = 10)
    
    mx = mr * math.sin(minute/360 * 3.14*2)
    my = mr * math.cos(minute/360 * 3.14*2)

    canvas.create_line(cx, cy, cx+mx, cy-my, fill='Green', width = 6)
    
    sx = sr * math.sin(second/360 * 3.14*2)
    sy = sr * math.cos(second/360 * 3.14*2)
    
    canvas.create_line(cx, cy, cx+sx, cy-sy, fill='Red', width = 2)

    canvas.create_arc(cx-10, cy-10, cx+10, cy+10, extent=359,style=CHORD, width = 2, fill = 'black')

    tk.update()    
    time.sleep(1)


