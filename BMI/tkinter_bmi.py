from tkinter import *
from math import *

tk = Tk()
tk.title("BMI")
tk.geometry("440x150")
tk.configure(background='orange')

height= StringVar()
bmi= StringVar()
mass = StringVar()
an = StringVar()


def label():
    Label(tk, text = "BMI",bg="orange", fg = "blue", font=("Arial", 20)).place(x= 190, y= 5)
    Label(tk, text = "Nhập vào:",bg="orange", font=("Times New Roman", 14)).place(x=10, y= 35)
    Label(tk, text = "Khối lượng:",bg="orange",font=("Tahoma", 10)).place(x=10, y= 60)
    Label(tk, text = "Chiều cao:",bg="orange", font=("Tahoma", 10)).place(x=10, y= 85)
    Label(tk, text = "BMI index:",bg="orange", font=("Tahoma", 10)).place(x=10, y= 110)
    Label(tk, text = "kg",bg="orange", font=("Tahoma", 9)).place(x=180, y= 60)
    Label(tk, text = "m" ,bg="orange", font=("Tahoma", 9)).place(x=180, y= 85)


def clear():
    mass.set("")
    height.set("")
    bmi.set("")
    an.set("")

def convert():
    b = float(bmi.get())
    if b < 18.5:
        an.set("You are " + "Thin.")
    elif (b >= 18.5) and (b <= 25):
        an.set("You are " + "Normal.")
    elif (b >= 25) and (b <= 30):
        an.set("You are " + "OverWeight")
    elif b>30:
        an.set("You are " + "fat.")
    else:
        an.set("You are " + "NOT a human.")

def entry():
    Entry(tk,width = 13, textvariable = mass).place(x=92, y= 63)
    Entry(tk,width = 13, textvariable = height).place(x=92, y= 88)
    Entry(tk,width = 15, textvariable = bmi).place(x=92, y= 113)
    Entry(tk,width = 22, textvariable = an).place(x=250, y= 113)

def button():
    Button(tk, width = 5, text = "Solve", bg = "lavender", command = solve).place(x = 250,y= 85)
    Button(tk, width = 5, text = "Clear", bg = "lavender", command = clear).place(x = 295,y= 85)
    Button(tk, width = 5, text = "Exit" , bg = "lavender", command = tk.quit).place(x = 340,y= 85)
    Button(tk, width = 4, text = " => " , command = convert).place(x = 200,y= 112)

def solve():
    h = float(height.get())
    w = float(mass.get())
    b = w/(h**2)
    bmi.set(b)


label()
entry()
button()
tk.mainloop()