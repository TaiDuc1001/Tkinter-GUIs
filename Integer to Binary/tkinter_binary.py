from tkinter import *
from PIL import Image
from PIL import ImageTk

tk = Tk()
tk.title("Binary")
tk.geometry("270x200")

inter  = StringVar()
binary = StringVar()

def label():
    Label(tk, text = "Integer to Binary",bg="lavender", fg = "orange", font=("Arial", 12)).place(x= 75, y= 2)
    Label(tk, text = "   Enter an integer:",bg="lavender", font=("Times New Roman", 9)).place(x=10, y= 24)
    Label(tk, text = "Binary:",bg="lavender", font=("Times New Roman", 9)).place(x=62, y= 52)

def button():
	Button(tk, width = 6, text = "Convert", bg = "gold", command = convert).place(x = 10,y= 49)
	Button(tk, width = 5, text = "Clear", bg = "lavender", command = clear).place(x = 220,y= 23)
	Button(tk, width = 5, text = "Exit", bg = "lavender", command = tk.quit).place(x = 220,y= 52)

def clear():
    inter.set("")
    binary.set("")

def convert():
	i = int(inter.get())
	b = bin(i)[2::]
	binary.set(b)

def entry():
	Entry(tk,width = 17, textvariable = inter ).place(x=102, y= 26)
	Entry(tk,width = 17, textvariable = binary).place(x=102, y= 54)

# photo = Image.open("v.jpg")
# photo = photo.resize((200,125), Image.ANTIALIAS)
# photoImg = ImageTk.PhotoImage(photo)
# Button(tk, image= photoImg, relief = RAISED).place(x = 360, y=5)
tk.configure(background='lavender')

label()
button()
entry()
tk.mainloop()
