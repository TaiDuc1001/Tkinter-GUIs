from tkinter import *
from math import *
import tkinter.messagebox as mbox

tk = Tk()
tk.geometry("155x143")
mass = StringVar()

def button():
	Button(tk, width = 4, text = "1"  , bg = "lavender", command = so1  ).place(x = 20 - 18,y= 35 )
	Button(tk, width = 4, text = "2"  , bg = "lavender", command = so2  ).place(x = 58 - 18,y= 35 )
	Button(tk, width = 4, text = "3"  , bg = "lavender", command = so3  ).place(x = 96 - 18,y= 35 )
	Button(tk, width = 4, text = "4"  , bg = "lavender", command = so4  ).place(x = 20 - 18,y= 62 )
	Button(tk, width = 4, text = "5"  , bg = "lavender", command = so5  ).place(x = 58 - 18,y= 62 )
	Button(tk, width = 4, text = "6"  , bg = "lavender", command = so6  ).place(x = 96 - 18,y= 62 )
	Button(tk, width = 4, text = "7"  , bg = "lavender", command = so7  ).place(x = 20 - 18,y= 89 )
	Button(tk, width = 4, text = "8"  , bg = "lavender", command = so8  ).place(x = 58 - 18,y= 89 )
	Button(tk, width = 4, text = "9"  , bg = "lavender", command = so9  ).place(x = 96 - 18,y= 89 )
	Button(tk, width = 4, text = "0"  , bg = "lavender", command = so0  ).place(x = 58 - 18,y= 116)
	Button(tk, width = 4, text = "Clr", bg = "lavender", command = clear).place(x = 20 - 18,y= 116)
	Button(tk, width = 4, text = "+"  , bg = "lavender", command = cong ).place(x = 134- 18,y= 35 )
	Button(tk, width = 4, text = "-"  , bg = "lavender", command = tru  ).place(x = 134- 18,y= 62 )
	Button(tk, width = 4, text = "x"  , bg = "lavender", command = nhan ).place(x = 134- 18,y= 89 )
	Button(tk, width = 4, text = "/"  , bg = "lavender", command = chia ).place(x = 134- 18,y= 116)
	Button(tk, width = 4, text = "="  , bg = "lavender", command = solve).place(x = 96 - 18,y= 116)
	Button(tk, width = 4, text = "DEL", bg = "lavender", command = Del  ).place(x = 134- 18,y= 8  )

def so1():
	a = mass.get()
	mass.set(a + "1")
def so2():
	a = mass.get()
	mass.set(a + "2")
def so3():
	a = mass.get()
	mass.set(a + "3")
def so4():
	a = mass.get()
	mass.set(a + "4")
def so5():
	a = mass.get()
	mass.set(a + "5")
def so6():
	a = mass.get()
	mass.set(a + "6")
def so7():
	a = mass.get()
	mass.set(a + "7")
def so8():
	a = mass.get()
	mass.set(a + "8")
def so9():
	a = mass.get()
	mass.set(a + "9")
def so0():
	a = mass.get()
	mass.set(a + "0")

def solve():
	a = mass.get()
	if "x" in a:
		mass.set(a + " = " + str(eval(a.replace("x","*"))))
	elif "/" in a:
		mass.set(a + " = " + str(round(eval(a.replace("x","*")), 5)))
	else:
		mass.set(a + " = " + str(eval(a)))
	a = mass.get()
	if len(a) > 19:
		mbox.showinfo('Too Much Characters', 'Your equation have too much characters!')

def chia():
	a = mass.get()
	if "+" in str(a):
		mass.set(a.replace("+", "/"))
	elif "x" in str(a):
		mass.set(a.replace("x", "/"))
	elif "-" in str(a):
		mass.set(a.replace("-", "/"))
	else:
		mass.set(a + " / ")

def cong():
	a = mass.get()
	if "-" in str(a):
		mass.set(a.replace("-", "+"))
	elif "x" in str(a):
		mass.set(a.replace("x", "+"))
	elif "/" in str(a):
		mass.set(a.replace("/", "+"))
	else:
		mass.set(a + " + ")

def tru():
	a = mass.get()
	if "+" in str(a):
		mass.set(a.replace("+", "-"))
	elif "x" in str(a):
		mass.set(a.replace("x", "-"))
	elif "/" in str(a):
		mass.set(a.replace("/", "-"))
	else:
		mass.set(a + " - ")

def nhan():
	a = mass.get()
	if "+" in str(a):
		mass.set(a.replace("+", "x"))
	elif "-" in str(a):
		mass.set(a.replace("-", "x"))
	elif "/" in str(a):
		mass.set(a.replace("/", "x"))
	else:
		mass.set(a + " x ")

def clear():
	mass.set("")

def Del():
	a = mass.get()
	mass.set(a[:-1])

Entry(tk,width = 17, textvariable = mass).place(x=25 - 19, y= 12)

button()
tk.mainloop()

