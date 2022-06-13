from tkinter import *
from math import *
from PIL import Image
from PIL import ImageTk
import tkinter.messagebox as mbox




def hs0():
	ngaysinh.set(f"{hs0_name}: {hs0_birthday}")
def hs1():
	ngaysinh.set(f"{hs1_name}: {hs1_birthday}")
def hs2():
	ngaysinh.set(f"{hs2_name}: {hs2_birthday}")
def hs3():
	ngaysinh.set(f"{hs3_name}: {hs3_birthday}")
def hs4():
	ngaysinh.set(f"{hs4_name}: {hs4_birthday}")
def hs5():
	ngaysinh.set(f"{hs5_name}: {hs5_birthday}")
def hs6():
	ngaysinh.set(f"{hs6_name}: {hs6_birthday}")
def hs7():
	ngaysinh.set(f"{hs7_name}: {hs7_birthday}")
def hs8():
	ngaysinh.set(f"{hs8_name}: {hs8_birthday}")
def hs9():
	ngaysinh.set(f"{hs9_name}: {hs9_birthday}")
def hs10():
	ngaysinh.set(f"{hs10_name}: {hs10_birthday}")
def hs11():
	ngaysinh.set(f"{hs11_name}: {hs11_birthday}")
def hs12():
	ngaysinh.set(f"{hs12_name}: {hs12_birthday}")
def hs13():
	ngaysinh.set(f"{hs13_name}: {hs13_birthday}")
def hs14():
	ngaysinh.set(f"{hs14_name}: {hs14_birthday}")
def hs15():
	ngaysinh.set(f"{hs15_name}: {hs15_birthday}")
def hs16():
	ngaysinh.set(f"{hs16_name}: {hs16_birthday}")
def hs17():
	ngaysinh.set(f"{hs17_name}: {hs17_birthday}")
def hs18():
	ngaysinh.set(f"{hs18_name}: {hs18_birthday}")
def hs19():
	ngaysinh.set(f"{hs19_name}: {hs19_birthday}")
def hs20():
	ngaysinh.set(f"{hs20_name}: {hs20_birthday}")
def hs21():
	ngaysinh.set(f"{hs21_name}: {hs21_birthday}")
def hs22():
	ngaysinh.set(f"{hs22_name}: {hs22_birthday}")
def hs23():
	ngaysinh.set(f"{hs23_name}: {hs23_birthday}")
def hs24():
	ngaysinh.set(f"{hs24_name}: {hs24_birthday}")
def hs25():
	ngaysinh.set(f"{hs25_name}: {hs25_birthday}")
def hs26():
	ngaysinh.set(f"{hs26_name}: {hs26_birthday}")
def hs27():
	ngaysinh.set(f"{hs27_name}: {hs27_birthday}")
def hs28():
	ngaysinh.set(f"{hs28_name}: {hs28_birthday}")
def hs29():
	ngaysinh.set(f"{hs29_name}: {hs29_birthday}")
def hs30():
	ngaysinh.set(f"{hs30_name}: {hs30_birthday}")
def hs31():
	ngaysinh.set(f"{hs31_name}: {hs31_birthday}")
def hs32():
	ngaysinh.set(f"{hs32_name}: {hs32_birthday}")
def hs33():
	ngaysinh.set(f"{hs33_name}: {hs33_birthday}")
def hs34():
	ngaysinh.set(f"{hs34_name}: {hs34_birthday}")
def hs35():
	ngaysinh.set(f"{hs35_name}: {hs35_birthday}")
def hs36():
	ngaysinh.set(f"{hs36_name}: {hs36_birthday}")
def hs37():
	ngaysinh.set(f"{hs37_name}: {hs37_birthday}")
def hs38():
	ngaysinh.set(f"{hs38_name}: {hs38_birthday}")
def hs39():
	ngaysinh.set(f"{hs39_name}: {hs39_birthday}")
def hs40():
	ngaysinh.set(f"{hs40_name}: {hs40_birthday}")
def hs41():
	ngaysinh.set(f"{hs41_name}: {hs41_birthday}")
def hs43():
	ngaysinh.set("Trần Hoàng Anh: 19/9/2005")

def co_diem():
	ngaysinh.set("Cô Nguyễn Thị Ngọc Diễm: ")
def send():
    mbox.showinfo('QUÝ ÔNGS B9 ==> CÁC BẠN NỮ B9', 'Chúc mừng Ngày Phụ Nữ Việt Nam 20/10 ❤🥰❤')




names = ['Vũ Trúc Lan Anh','Lê Hữu Thiện Ân','Phạm Thái Duy Bảo','Đỗ Ngọc Phương Chi',
		'Lê Chí Đại','Thái Thành Đạt','Hà Tấn Đạt','Nguyễn Thị Hồng Diễm','Phan Tài Đức','Đào Quang Dương',
		'Nguyễn Quốc Bảo Duy','Nguyễn Thuý Hằng','Trần Thị Diễm Hương','Lê Nguyên Hương','Lê Thanh Huyền',
		'Phan Hoàng Quốc Khánh','Đỗ Đăng Khoa','Nguyễn Đức Anh Khôi','Lê Hoàng Minh Khôi','Phan Quỳnh Khánh Linh'
		,'Lý Quang Minh','Trần Văn Nam','Lê Quang Nhật','Lương Minh Nhật','Hà Bảo Nhi','Đỗ Hồng Nhung','Nguyễn Thành Phát'
		,'Bửu Huỳnh Vĩnh Phúc','Võ Thị Yến Quyên','Đoàn Công Thiện','Nguyễn Thị Minh Thư','Trần Ngọc Anh Thư','Phan Thị Minh Thư'
		,'Lý Ngọc Mỹ Thuận','Tạ Khánh Linh Thy','Trần Trọng Tín','Trần Duy Trí','Ngô Thị Kiều Trinh','Phan Trần Quốc Tuấn'
		,'Nguyễn Nhật Uyên','Huỳnh Hồng Yến','Nguyễn Lê Bảo Yến']

birdays = ['15/11/2005','25/6/2005','1/2/2005','13/3/2005','30/6/2005','15/10/2005','13/10/2005','9/1/2005',
			'9/11/2005','10/11/2005','1/4/2005','14/3/2005','23/6/2005','10/6/2005','26/6/2005','14/9/2005',
			'3/10/2005','30/12/2005','8/1/2005','19/7/2005','24/2/2005','29/7/2005','27/6/2005','6/4/2005',
			'23/5/2005','1/3/2005','30/1/2005','16/6/2005','1/11/2005','2/9/2005','26/1/2005','11/10/2005',
			'1/9/2005','11/2/2005','25/6/2005','20/10/2005','17/9/2005','11/1/2005','27/12/2005','27/8/2005',
			'12/1/2005','17/6/2005']




hs0_name , hs0_birthday  = names[0] , birdays[ 0]
hs1_name , hs1_birthday  = names[1] , birdays[ 1]
hs2_name , hs2_birthday  = names[2] , birdays[ 2]
hs3_name , hs3_birthday  = names[3] , birdays[ 3]
hs4_name , hs4_birthday  = names[4] , birdays[ 4]
hs5_name , hs5_birthday  = names[5] , birdays[ 5]
hs6_name , hs6_birthday  = names[6] , birdays[ 6]
hs7_name , hs7_birthday  = names[7] , birdays[ 7]
hs8_name , hs8_birthday  = names[8] , birdays[ 8]
hs9_name , hs9_birthday  = names[9] , birdays[ 9]

hs10_name, hs10_birthday = names[10], birdays[10]
hs11_name, hs11_birthday = names[11], birdays[11]
hs12_name, hs12_birthday = names[12], birdays[12]
hs13_name, hs13_birthday = names[13], birdays[13]
hs14_name, hs14_birthday = names[14], birdays[14]
hs15_name, hs15_birthday = names[15], birdays[15]
hs16_name, hs16_birthday = names[16], birdays[16]
hs17_name, hs17_birthday = names[17], birdays[17]
hs18_name, hs18_birthday = names[18], birdays[18]
hs19_name, hs19_birthday = names[19], birdays[19]
hs20_name, hs20_birthday = names[20], birdays[20]

hs21_name, hs21_birthday = names[21], birdays[21]
hs22_name, hs22_birthday = names[22], birdays[22]
hs23_name, hs23_birthday = names[23], birdays[23]
hs24_name, hs24_birthday = names[24], birdays[24]
hs25_name, hs25_birthday = names[25], birdays[25]
hs26_name, hs26_birthday = names[26], birdays[26]
hs27_name, hs27_birthday = names[27], birdays[27]
hs28_name, hs28_birthday = names[28], birdays[28]
hs29_name, hs29_birthday = names[29], birdays[29]
hs30_name, hs30_birthday = names[30], birdays[30]

hs31_name, hs31_birthday = names[31], birdays[31]
hs32_name, hs32_birthday = names[32], birdays[32]
hs33_name, hs33_birthday = names[33], birdays[33]
hs34_name, hs34_birthday = names[34], birdays[34]
hs35_name, hs35_birthday = names[35], birdays[35]
hs36_name, hs36_birthday = names[36], birdays[36]
hs37_name, hs37_birthday = names[37], birdays[37]
hs38_name, hs38_birthday = names[38], birdays[38]
hs39_name, hs39_birthday = names[39], birdays[39]
hs40_name, hs40_birthday = names[40], birdays[40]
hs41_name, hs41_birthday = names[41], birdays[41]


x_column_1 = 5
x_column_2 = x_column_1 + 33
x_column_3 = x_column_2 + 70
x_column_4 = x_column_3 + 33
x_column_5 = x_column_4 + 70
x_column_6 = x_column_5 + 33
x_column_7 = x_column_6 + 70
x_column_8 = x_column_7 + 33

y_row_1 = 40
y_row_2 = y_row_1 + 29
y_row_3 = y_row_2 + 29
y_row_4 = y_row_3 + 29
y_row_5 = y_row_4 + 29
y_row_6 = y_row_5 + 29
y_row_7 = y_row_6 + 29
y_row_8 = y_row_7 + 29
y_row_9 = y_row_8 + 29
y_row_10 = y_row_9 + 29
y_row_11 = y_row_10 + 29


# tạo tkinter

tk = Tk()
ngaysinh = StringVar()

width_button = 3
bg_color_m = '#C8C8C8'
bg_color_g = '#DD9BB1'
photo = Image.open("C:\\Users\\DucPhan\\Downloads\\line1.png")
photo_2 = Image.open("C:\\Users\\DucPhan\\Downloads\\present3.jpg")
photo = photo.resize((1200,800), Image.ANTIALIAS)
photo_2 = photo_2.resize((80,60), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(photo)
photoImg_2 = ImageTk.PhotoImage(photo_2)
tk.resizable(height=True, width = True)
tk.minsize(height = 650, width = 900)

tk.title("HAPPY 20/10 AT 11B9")
Label(tk, image= photoImg, relief = RAISED).place(x= 0, y= -110)


Entry(tk ,bg= "#F2A793",bd = 5,textvariable = ngaysinh,justify = CENTER).place(x=14, y= 300,width = 370,height=300)

Button(tk, width = 7, text = "CÔ DIỄM", bg = bg_color_g, command = co_diem).place(x = 7,y = 5)

Button(tk, image = photoImg_2, command = send).place(x = 810,y = 580) #hop qua
# tổ 1
Button(tk, width = width_button, text = "39", bg = bg_color_m, command = hs38).place(x = x_column_1,y = y_row_1)
Button(tk, width = width_button, text = "30", bg = bg_color_m, command = hs29).place(x = x_column_2,y = y_row_1)
Button(tk, width = width_button, text = "26", bg = bg_color_g, command = hs25).place(x = x_column_1,y = y_row_2)  #girl
Button(tk, width = width_button, text = "38", bg = bg_color_g, command = hs37).place(x = x_column_2,y = y_row_2)  #girl
Button(tk, width = width_button, text = "20", bg = bg_color_g, command = hs19).place(x = x_column_1,y = y_row_3)  #girl
Button(tk, width = width_button, text = "40", bg = bg_color_g, command = hs39).place(x = x_column_2,y = y_row_3)  #girl
Button(tk, width = width_button, text = "15", bg = bg_color_g, command = hs14).place(x = x_column_1,y = y_row_4)  #girl
Button(tk, width = width_button, text = "14", bg = bg_color_g, command = hs13).place(x = x_column_2,y = y_row_4)  #girl
Button(tk, width = width_button, text = "08", bg = bg_color_g, command = hs7 ).place(x = x_column_1,y = y_row_5)  #girl
Button(tk, width = width_button, text = "35", bg = bg_color_g, command = hs34).place(x = x_column_2,y = y_row_5)  #girl
Button(tk, width = width_button, text = "03", bg = bg_color_m, command = hs2 ).place(x = x_column_1,y = y_row_6)
# tổ 2
Button(tk, width = width_button, text = "29", bg = bg_color_g, command = hs28).place(x = x_column_3,y = y_row_1)  #girl
Button(tk, width = width_button, text = "36", bg = bg_color_m, command = hs35).place(x = x_column_4,y = y_row_1)
Button(tk, width = width_button, text = "34", bg = bg_color_g, command = hs33).place(x = x_column_3,y = y_row_2)  #girl
Button(tk, width = width_button, text = "06", bg = bg_color_m, command = hs5 ).place(x = x_column_4,y = y_row_2)
Button(tk, width = width_button, text = "33", bg = bg_color_g, command = hs32).place(x = x_column_3,y = y_row_3)  #girl
Button(tk, width = width_button, text = "01", bg = '#fce5ff' , command = hs43).place(x = x_column_4,y = y_row_3)
Button(tk, width = width_button, text = "05", bg = bg_color_m, command = hs4 ).place(x = x_column_3,y = y_row_4)
Button(tk, width = width_button, text = "10", bg = bg_color_m, command = hs9 ).place(x = x_column_4,y = y_row_4)
Button(tk, width = width_button, text = "02", bg = bg_color_m, command = hs1 ).place(x = x_column_3,y = y_row_5)
Button(tk, width = width_button, text = "37", bg = bg_color_m, command = hs36).place(x = x_column_4,y = y_row_5)
# tổ 3
Button(tk, width = width_button, text = "01", bg = bg_color_g, command = hs0 ).place(x = x_column_5,y = y_row_1)  #girl
Button(tk, width = width_button, text = "42", bg = bg_color_g, command = hs41).place(x = x_column_6,y = y_row_1)  #girl
Button(tk, width = width_button, text = "04", bg = bg_color_g, command = hs3 ).place(x = x_column_5,y = y_row_2)  #girl
Button(tk, width = width_button, text = "13", bg = bg_color_g, command = hs12).place(x = x_column_6,y = y_row_2)  #girl
Button(tk, width = width_button, text = "25", bg = bg_color_g, command = hs24).place(x = x_column_5,y = y_row_3)  #girl
Button(tk, width = width_button, text = "12", bg = bg_color_g, command = hs11).place(x = x_column_6,y = y_row_3)  #girl
Button(tk, width = width_button, text = "31", bg = bg_color_g, command = hs30).place(x = x_column_5,y = y_row_4)  #girl
Button(tk, width = width_button, text = "41", bg = bg_color_g, command = hs40).place(x = x_column_6,y = y_row_4)  #girl
Button(tk, width = width_button, text = "17", bg = bg_color_m, command = hs16).place(x = x_column_5,y = y_row_5)
Button(tk, width = width_button, text = "18", bg = bg_color_m, command = hs17).place(x = x_column_6,y = y_row_5)
Button(tk, width = width_button, text = "28", bg = bg_color_m, command = hs27).place(x = x_column_5,y = y_row_6)
Button(tk, width = width_button, text = "23", bg = bg_color_m, command = hs22).place(x = x_column_6,y = y_row_6)
# tổ 4
Button(tk, width = width_button, text = "24", bg = bg_color_m, command = hs23).place(x = x_column_7,y = y_row_1)
Button(tk, width = width_button, text = "22", bg = bg_color_m, command = hs21).place(x = x_column_8,y = y_row_1)
Button(tk, width = width_button, text = "21", bg = bg_color_m, command = hs20).place(x = x_column_7,y = y_row_2)
Button(tk, width = width_button, text = "09", bg = bg_color_m, command = hs8 ).place(x = x_column_8,y = y_row_2)
Button(tk, width = width_button, text = "27", bg = bg_color_m, command = hs26).place(x = x_column_7,y = y_row_3)
Button(tk, width = width_button, text = "07", bg = bg_color_m, command = hs6 ).place(x = x_column_8,y = y_row_3)
Button(tk, width = width_button, text = "11", bg = bg_color_m, command = hs10).place(x = x_column_7,y = y_row_4)
Button(tk, width = width_button, text = "16", bg = bg_color_m, command = hs15).place(x = x_column_8,y = y_row_4)
Button(tk, width = width_button, text = "32", bg = bg_color_g, command = hs31).place(x = x_column_7,y = y_row_5)  #girl
Button(tk, width = width_button, text = "19", bg = bg_color_m, command = hs18).place(x = x_column_8,y = y_row_5)



mainloop()
