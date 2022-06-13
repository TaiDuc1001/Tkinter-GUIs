from tkinter import *
from math import sqrt
import tkinter.messagebox as mbox
from PIL import Image
from PIL import ImageTk

tk = Tk()
tk.title("Einstein")
tk.geometry("550x250")
tk.configure(background='lavender')

real_m = StringVar()
speed_m = StringVar()
relative_m = StringVar()

real_l = StringVar()
speed_l  = StringVar()
relative_l = StringVar()

def label():
    Label(tk, text = "Relative mass" ,bg="lavender", fg = "orange", font=("Arial", 12)).place(x= 100, y= 2)
    Label(tk, text = "Real mass(kg):"    ,bg="lavender", font=("Times New Roman", 9)).place(x=9, y= 24)
    Label(tk, text = "Speed (m/s):",bg="lavender", font=("Times New Roman", 9)).place(x=9, y= 52)
    Label(tk, text = "Relative mass(kg):",bg="lavender", font=("Times New Roman", 9)).place(x=9, y= 78)

    Label(tk, text = "Relative lenght" ,bg="lavender", fg = "orange", font=("Arial", 12)).place(x= 371, y= 2)
    Label(tk, text = "Real lenght(m):" ,bg="lavender", font=("Times New Roman", 9)).place(x=280, y= 24)
    Label(tk, text = "Speed (m/s):",bg="lavender", font=("Times New Roman", 9)).place(x=280, y= 52)
    Label(tk, text = "Relative lenght(m):",bg="lavender", font=("Times New Roman", 9)).place(x=280, y= 78)

def button():
    Button(tk, width = 5, text = "Solve", bg = "lavender", command = solve_1).place(x = 215,y= 22)
    Button(tk, width = 5, text = "Clear", bg = "lavender", command = clear_1).place(x = 215,y= 51)

    Button(tk, width = 5, text = "Solve", bg = "lavender", command = solve_2).place(x = 488,y= 22)
    Button(tk, width = 5, text = "Clear", bg = "lavender", command = clear_2).place(x = 488,y= 51)

def clear_1():
    real_m.set("")
    relative_m.set("")
    speed_m.set("")

def solve_1(): 
    a1 = int(real_m.get())
    v1 = int(speed_m.get())
    c = int(299792458)
    try:
        b1 = a1 / sqrt(1- ((v1**2)/(c**2)))
        relative_m.set(b1)
    except:
        relative_m.set("Error")
        mbox.showinfo('Max speed', 'Speed has larger than Light Speed ' + '( ' + str(v1) + ' > ' + str(c) +')')

def solve_2():
    a2 = int(real_l.get())
    v2 = int(speed_l.get())
    c = int(299792458)
    try:
        b2= a2 * sqrt(1- ((v2**2)/(c**2)))
        relative_l.set(b2)
    except:
        relative_l.set("Error")
        mbox.showinfo('Max speed', 'Speed has larger than Light Speed ' + '( ' + str(v2) + ' > ' + str(c) +')')

def clear_2():
    real_l.set("")
    relative_l.set("")
    speed_l.set("")   

def entry():
    Entry(tk,width = 17, textvariable = real_m ).place(x=102, y= 26)
    Entry(tk,width = 17, textvariable = speed_m).place(x=102, y= 54)
    Entry(tk,width = 17, textvariable = relative_m).place(x=102, y= 80)

    Entry(tk,width = 17, textvariable = real_l ).place(x=375, y= 26)
    Entry(tk,width = 17, textvariable = speed_l).place(x=375, y= 54)
    Entry(tk,width = 17, textvariable = relative_l).place(x=375, y= 80)

def can():
    can = Canvas(tk)
    can.create_line(275, 20, 275, 100)
    can.pack(fill=BOTH, expand=1)
    can.configure(background='lavender')

# photo = Image.open("Fire.jpg")
# photo = photo.resize((40,30 ), Image.ANTIALIAS)
# photoImg = ImageTk.PhotoImage(photo)
# Button(tk, image= photoImg, relief = RAISED).place(x = 50, y=200)

can()
label()
entry()
button()
tk.mainloop()