from tkinter import *
from math import *

tk = Tk()
so_a = IntVar()
so_b = IntVar()
ketqua = IntVar()

tk.resizable(height=True, width = True)
tk.minsize(height = 165, width = 200)
tk.title("Cộng trừ nhân chia!")



def addition():
	a= int(so_a.get())
	b= int(so_b.get())
	ketqua.set(str(a+b))

def subtraction():
	a= int(so_a.get())
	b= int(so_b.get())
	ketqua.set(str(a-b))

def multiplication():
	a= int(so_a.get())
	b= int(so_b.get())
	ketqua.set(str(a*b))

def division():
	a= int(so_a.get())
	b= int(so_b.get())
	ketqua.set(str(a/b))

def Next():
	so_a.set("")
	so_b.set("")
	ketqua.set("")

Label(tk, text= "Cộng trừ nhân chia",fg="blue" ,font = ("tahoma", 15), justify = CENTER).grid(row = 0, columnspan = 3)

fb = Frame(tk)
fb.grid(rowspan= 3, column = 0)
Button(fb, text = "Cộng", command = addition).pack(side=TOP, fill = X)
Button(fb, text = "Trừ", command = subtraction).pack(side=TOP, fill = X)
Button(fb, text = "Nhân", command = multiplication).pack(side=TOP, fill = X)
Button(fb, text = "Chia", command = division).pack(side=TOP, fill = X)

Label(tk, text="number a: ").grid(row = 1, column = 1)
Label(tk, text="number b: ").grid(row = 2, column = 1)
Label(tk, text="Result: ").grid(row = 3, column = 1)
Button(tk, text = "Exit", command = tk.quit).grid(row = 4, column = 2)
Button(tk, text = "Clear", command = Next).grid(row = 4, column = 1)

Entry(tk, width = 15, textvariable = so_a).grid(row = 1, column = 2)
Entry(tk, width = 15, textvariable = so_b).grid(row = 2, column = 2)
Entry(tk, width = 15, textvariable = ketqua).grid(row = 3, column = 2)


Next()
tk.mainloop()
