from tkinter import *
from math import *
# from PIL import Image
# from PIL import ImageTk

tk = Tk()
tk.title("Physical")
tk.geometry("400x145")

x_button=220

speed= StringVar()
force= StringVar()
mass = StringVar()


def label():
	Label(tk, text = "Vận tốc lăn của 1 vật thể dưới 1 lực tác động", fg = "red", font=("Arial", 13)).place(x=10, y= 10)
	Label(tk, text = "Nhập vào:", font=("Times New Roman", 12)).place(x=10, y= 35)
	Label(tk, text = "Vận tốc lăn  :", font=("Tahoma", 10)).place(x=10, y= 110)
	Label(tk, text = "Lực tác động:", font=("Tahoma", 10)).place(x=10, y= 85)
	Label(tk, text = "Khối lượng   :", font=("Tahoma", 10)).place(x=10, y= 60)
	Label(tk, text = "m/s", font=("Tahoma", 9)).place(x=180, y= 114)
	Label(tk, text = "Joule", font=("Tahoma", 9)).place(x=180, y= 88)
	Label(tk, text = "kg", font=("Tahoma", 9)).place(x=180, y= 60)

def clear():
	speed.set("")
	force.set("")
	mass.set("")

def entry():
	Entry(tk,width = 13, textvariable = mass).place(x=92, y= 63)
	Entry(tk,width = 13, textvariable = force).place(x=92, y= 88)
	Entry(tk,width = 13, textvariable = speed ).place(x=92, y= 113)
 
def speed_f():
	f = int(str(force.get()))
	m = int(str(mass.get()))
	s = sqrt((2*f)/m)
	speed.set(round(s, 9))

def mass_f():
	f=int(str(force.get()))
	s=int(str(speed.get()))
	m = (2*f)/(s**2)
	mass.set(round(m, 9))

def force_f():
	s=int(str(speed.get()))
	m=int(str(mass.get()))
	f = ((s**2)*m)/2
	force.set(round(f, 9))

def button():
	Button(tk, width = 5, text = "mass", bg = "lavender", command = mass_f  ).place(x = 270,y= 57)
	Button(tk, width = 5, text = "force", bg = "lavender", command = force_f  ).place(x = 270,y= 84)
	Button(tk, width = 5, text = "speed", bg = "lavender", command = speed_f  ).place(x = 270,y= 111)
	Button(tk, width = 5, text = "Clear", bg = "lavender", command = clear  ).place(x = x_button,y= 70)
	Button(tk, width = 5, text = "Exit" , bg = "lavender", command = tk.quit).place(x = x_button,y= 97)

# photo = Image.open("v.jpg")
# photo = photo.resize((200,125), Image.ANTIALIAS)
# photoImg = ImageTk.PhotoImage(photo)
# Button(tk, image= photoImg, relief = RAISED).place(x = 360, y=5)

label()
entry()
button()
tk.mainloop()