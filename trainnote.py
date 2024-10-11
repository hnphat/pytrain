def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n > 1: return fibo(n-1) + fibo(n-2)
    else: return "n <= 1"

def nonFunction(): # Hàm không có nội dung
    pass

print("""
Kiểu chuỗi dạng 
      đoạn văn
        nhiều dòng
      """)

def pow(x,y):
    try:
        result = 1
        if x < 0 or y < 0: return 0
        for i in range(0,y):
            result = result * x
        return result
    except:
        return 0

def powToFile(url,x,y):    
    file = open(url,"w",encoding="utf-8")
    file.write("Tính pow \n")
    file.write("X = " + str(x) + "\n")
    file.write("Y = " + str(y) + "\n")
    file.write("Result = " + str(pow(x,y)))
    file.close()

def checkCMND(cmnd):
    try:
        x = int(cmnd)
    except:
        x = 0
    if x == 0: print("Số CMND không hợp lệ")
    else:
        if len(cmnd) >= 9 and len(cmnd) <= 12: print("CMND hợp lệ")
        else:
            print("CMND không hợp lệ")

def checkMail(mail):
    if (mail.find("@") < 0 or mail.count("@") > 1):
        print("Email không hợp lệ")
    else:
        str = mail.split("@")
        if (str[0] == "" or str[1] == ""): print("Địa chỉ và tên miền không được trống")
        elif (str[1].find(".") < 0 or str[1].count(".") > 1): print("Tên miền email không hợp lệ")
        else: print("Email hợp lệ")

set1 = {1,2,3,4,5,"ABC",2.5,(1,2),True} 
# Không sử dụng List trong Set (tập hợp)
# Các giá trị trong tập hợp phải là các giá trị không thể thay đổi. Tập hợp thì có thể thêm bớt phần tử
# Giá trị trong tập hợp là duy nhất (thêm trùng tập hợp tự bỏ)
# Các phần tử trong tập hợp hổn loạn và không có thứ tự
# Có thể sử dụng các phép toán trong tập hợp như: giao, hiệu, hợp
list1 = [1,2,3,4,5,(1,2),{"a":1},True] # Như kiểu array gọi là list => sử dụng đc cách hàm thay đổi giá trị trong list
tuple1 = (1,2,3,4,5, (1,2), [1,2], {"A":1},True) 
# Không thể thay đổi sau khi khởi tạo tuple => có thể thay đổi giá trị của list nằm bên trong tuple
# Chỉ sử dụng được hàm lấy giá trị như len, index,...
# tuple truy nhất nhanh hơn list
# thích hợp khai báo hằng, dãy hằng

dict1 = dict({"A": "Apple", "A": "Apple", "C": [1,2,3], "D": (1,2,3,4), "E": {1,2,3,4,5}, "F": 2.5, "G": dict({"A":1}), "H": True})
#Khoá của dict có thể là chuỗi hoặc số và phải là duy nhất


# BÀI TẬP 1
colectionBank = dict({"laisuat": 0.0046, "sothanggui": 12})
try:
    tienvon = int(input("Nhập số tiền gửi bank: "))
except:
    tienvon = 0
tienlaithang = tienvon * colectionBank["laisuat"]
tongtiencoduoc = (colectionBank["sothanggui"] * tienlaithang) + tienvon
print("Tổng tiền có được sau 18 tháng")
print("Tiền vốn: {:,}".format(tienvon)," tiền lãi hàng tháng: {:,}".format(int(tienlaithang)), " sau 18 tháng có được: {:,}".format(int(tongtiencoduoc)))

# BÀI TẬP 2
print("Nhập họ và tên")
name = input()
# Xử lý khoảng trắng 02 bên trái phải
name = name.strip()
# Chữ đầu mỗi từ viết hoa
name = name.title()
# Xử lý phần đệm không dư khoảng trắng
tachChuoi = name.split()
name = " ".join(tachChuoi)
print("Kết quả: ", name)


# Bài toán tính số ngày từ tháng và năm nhập từ bàn phím
def checkNamNhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0):
        return True
    return False

# thang = int(input("Nhập tháng: "))
# nam = int(input("Nhập năm: "))
# songay = 0
# if (thang in [1,3,5,7,8,10,12]):
#     songay = 31
# elif (thang in [4,6,9,11]):
#     songay = 30
# else:
#     if (checkNamNhuan(nam)):
#         songay = 29
#     else:
#         songay = 28
# print("Số ngày: ",songay)

# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# pheptinh = input("Nhập phép tính + - * /: ")
# if (pheptinh not in ["+","-","*","/"]):
#     print("Phép tính không hợp lệ")
# else:
#     if (pheptinh == "+"): print("Kết quả: ", a+b)
#     if (pheptinh == "-"): print("Kết quả: ", a-b)
#     if (pheptinh == "*"): print("Kết quả: ", a*b)
#     if (pheptinh == "/"): print("Kết quả: ", a/b)

# # Tính tiền điện tiêu thụ
# bangGiaDien = dict({"I": 2000, "II": 2500, "III": 3000, "IV": 3500, "V": 4000})
# dienTieuThu = int(input("Nhập số điện tiêu thụ: "))
# if dienTieuThu <= 50:
#     print("Tiền điện: {:,}".format(dienTieuThu*bangGiaDien["I"]))
# elif dienTieuThu > 50 and dienTieuThu <= 150:
#     print("Tiền điện: {:,}".format(dienTieuThu*bangGiaDien["II"]))
# elif dienTieuThu > 150 and dienTieuThu <= 250:
#     print("Tiền điện: {:,}".format(dienTieuThu*bangGiaDien["III"]))
# elif dienTieuThu > 250 and dienTieuThu <= 350:
#     print("Tiền điện: {:,}".format(dienTieuThu*bangGiaDien["IV"]))
# else: print("Tiền điện: {:,}".format(dienTieuThu*bangGiaDien["V"]))

# Bài tính số tháng cần gửi bank để có được số tiền muốn có
# LAISUAT = float(input("Nhập lãi suất ngân hàng: "))
# tien = int(input("Nhập số tiền gửi bank: "))
# tienMuonCo = int(input("Nhập số tiền muốn có được: "))
# soThangCanGui = 0
# if (tien >= tienMuonCo): print("Số tiền muốn có thấp hơn hoặc bằng số tiền gửi ngân hàng => vô lý")
# else:
#     tienLaiHangThang = tien*LAISUAT
#     soThangCanGui = (tienMuonCo-tien)//tienLaiHangThang
#     print("Số tháng cần gửi để đạt được số tiền muốn có {:,}".format(tienMuonCo), " là ", soThangCanGui, " tháng")

# Bài nhập tháng để xem thuộc mùa nào
# MUA = dict({"Mùa xuân": (1,2,3), "Mùa hạ": (4,5,6), "Mùa thu": (7,8,9), "Mùa đông": (10,11,12)})
# try: thang = int(input("Nhập tháng: "))
# except: thang = 0
# if thang >= 1 and thang <= 12:
#     for guess in MUA:
#         if thang in MUA[guess]:
#             print("Tháng ", thang , " thuộc ", guess)
#             break
# else: print("Không tồn tại tháng này!")

# [KHÔNG ĐƠN GIẢN] Bài toán gửi tiền trong ngân hàng sau 05 năm sẽ được bao nhiêu
# LAISUAT = 0.9/100
# SOTHANG = 60
# tiengui = 8000000
# for i in range(SOTHANG):
#     tiengui = tiengui + tiengui*LAISUAT
# print("Sau 05 năm nhận được số tiền là {:,}".format(round(int(tiengui),-3)))

# Bài tính tuổi từ năm sinh
# from datetime import datetime
# year = datetime.now().year
# while True:
#     try:
#         namsinh = int(input("Nhập năm sinh: "))
#     except:
#         namsinh = 1900
#     if (namsinh > 1900 and namsinh <= year):
#         break
# print("Tuổi của bạn là: ", year - namsinh)

# Nhập thời gian theo dạng hh:mm:ss sao đó nhập số giây để sinh ra thời gian mới
# Hơi khó
# def isValidTime(thoigian):
#     if (len(thoigian) != 8):
#         return False
#     else:
#         if (thoigian.count(":") != 2):
#             return False
#         else:
#             tach = thoigian.split(":")
#             flag = True
#             for i in tach:
#                 try: 
#                     int(i)
#                 except:
#                     flag = False
#                     break
#                 if (len(i) != 2):
#                     flag = False
#                     break
#             if flag == False: 
#                 return False
#             else:
#                 gio = int(tach[0])
#                 phut = int(tach[1])
#                 giay = int(tach[2])
                
#                 if (gio < 0 or gio > 24): return False
#                 if (phut < 0 or phut > 59): return False
#                 if (giay < 0 or giay > 59): return False
#                 return True
                
# def calcToTime(thoigian, k):
#     tach = thoigian.split(":")
#     tongsogiay = k + int(tach[2])
#     sodu = tongsogiay % 60 
#     sophut = 0
#     if tongsogiay >= 60:
#         sophut = tongsogiay // 60    
#     giay = sodu
#     phut = int(tach[1]) + sophut
#     gio = 0
#     tempgio = 0
#     if (phut >= 60):
#         tempgio = tempgio + (phut // 60)
#         phut = phut % 60
#     if (tempgio != 0):
#         if (int(tach[0]) + tempgio) > 23:
#             gio = (int(tach[0]) + tempgio) % 24
#         else:
#             gio = (int(tach[0]) + tempgio)
#     else:
#         gio = int(tach[0])
#     if gio < 10:
#         gio = "0" + str(gio)
#     if phut < 10:
#         phut = "0" + str(phut)
#     if giay < 10:
#         giay = "0" + str(giay)
#     return str(gio) + ":" + str(phut) + ":" + str(giay)
    
# thoigian = input("Nhập thời gian (VD: hh:mm:ss): ")
# while not isValidTime(thoigian):
#     thoigian = input("Thời gian không đúng, vui lòng nhập lại (VD: hh:mm:ss): ")
# k = 0
# while k == 0:
#     try:
#         k = int(input("Nhập số giây bổ sung: "))
#     except:
#         k = 0
# print("Thời gian hiện tại là: ", calcToTime(thoigian,k))

# import tkinter as tk
# from tkinter import messagebox

# def onClick():
#     print("Tính tổng")
#     try:
#         a = int(textA.get(1.0))
#         b = int(textB.get(1.0))
#     except:
#         messagebox.showerror("Lỗi","Nhập sai lấy giá trị mặc định = 0")
#         return
#     textKQ.delete(1.0)
#     textKQ.insert(1.0,a+b)
# window = tk.Tk()
# window.title("Xin chao")

# labelA = tk.Label(text="Nhập A: ")
# labelA.place(x=5,y=5,width=100,height=20)

# textA = tk.Text()
# textA.place(x=80, y=5,width=100,height=20)

# labelB = tk.Label(text="Nhập B: ")
# labelB.place(x=5, y=30,width=100,height=20)

# textB = tk.Text()
# textB.place(x=80,y=30,width=100,height=20)

# but = tk.Button(text="Tính", command=onClick)
# but.place(x=60,y=60,width=50,height=20)


# labelKQ = tk.Label(text="Kết quả: ")
# labelKQ.place(x=40,y=90,width=100,height=30)

# textKQ = tk.Text()
# textKQ.place(x=120,y=90,width=100,height=30)

# textA.focus()
# print("ll" in "Hello")
# window.geometry("400x500")
# window.mainloop()

# sử dụng pandas
# import pandas as pd

# database = pd.read_csv("data.txt",sep=",",header=None,names=["HOTEN","LOP","TUOI","DIACHI"])
# ds_xapsep = database.sort_values("TUOI")
# dssv = ds_xapsep.query('LOP == "12B"')
# dslop = ds_xapsep["LOP"].unique()
# print(dslop)

# Tìm ước chung lớn nhất
# def timUoc(num):
#     uoc = []
#     for i in range(1,num+1):
#         if (num % i == 0):
#             uoc.append(i)
#     return set(uoc)

# def timUocChungMax(seta, setb):
#     uocChung = seta.intersection(setb)
#     return max(uocChung)

# try:
#     a = int(input("Nhập số đầu tiên: "))
# except:
#     a = 0
# try:
#     b = int(input("Nhập số thứ hai: "))
# except:
#     b = 0
# uoca = timUoc(a)
# uocb = timUoc(b)
# print("Ước chung lớn nhất: ",timUocChungMax(uoca,uocb))

# Bài toán 
# while (True):
#     try:
#         n = int(input("Nhập số nguyên dương: "))
#     except:
#         n = 0
#     if (n > 0): break

# print("N có ", len(str(n)), " chữ số")
# tong = 0
# for i in str(n):
#     tong = tong + int(i)
# print("Tổng: ", tong)

# Bài toán
# x = int(input("Nhập x: "))
# n = int(input("Nhập n: "))
# arr = []
# for i in range(0,n+1):
#     arr.append(x**(2*i+1))
# print("{:,}".format(sum(arr)))

# Bài mới
# n = int(input("Nhập số n: "))
# data = []
# for i in range(0,n):
#     data.append(float(input("Nhập thông tin " + str(i+1) + ": ")))
# print("Phần tử lớn nhất: ", max(data))
# print("Tổng các phần tử: ", sum(data))
# print("Sắp xếp tăng dần: ", sorted(data))
# soduong = 0
# soam = 0
# for i in data:
#     if (i > 0): soduong = soduong + 1
#     elif (i < 0): soam = soam + 1
# print("Số dương: ",soduong, " số; Số âm: ",soam, " số")


# Bài toán
# hangHoa = []
# sum = 0
# while(True):
#     matHang = {} #Đây là dict
#     matHang["Tên hàng"] = input("Tên hàng hoá: ")
#     if (matHang["Tên hàng"] == ""): break
#     try:
#         matHang["Số lượng"] = int(input("Số lượng hàng: "))
#     except:
#         matHang["Số lượng"] = 0
#     if (matHang["Số lượng"] == 0): break
#     try:
#         matHang["Giá bán"] = int(input("Giá bán: "))
#     except:
#         matHang["Giá bán"] = 0
#     sum = sum + matHang["Số lượng"]    
#     hangHoa.append(matHang)

# print("Tổng số lượng hàng hoá: ", sum)
# nho = []
# lon = []
# for i in hangHoa:
#     if (i["Số lượng"] < 10): 
#        nho.append(i["Tên hàng"])
#     if (i["Số lượng"] > 50): 
#         lon.append(i["Tên hàng"])
# print("Các mặt hàng có số lượng nhỏ hơn 10: ", nho)
# print("Các mặt hàng có số lượng lớn hơn 50: ", lon)


# Bài toán
# def xepLoai(diem):
#     if (diem >= 9): return "Xuất sắc"
#     if (diem >=8 and diem < 9): return "Giỏi"
#     if (diem >=7 and diem < 8): return "Khá"
#     if (diem >=5 and diem < 7): return "Trung bình"
#     if (diem < 5): return "Yếu"

# danhSach = []
# while(True):
#     chiTiet = {}
#     chiTiet["Tên học sinh"] = input("Nhập tên học sinh: ")
#     if (chiTiet["Tên học sinh"] == ""): break
#     chiTiet["Toán"] = float(input("Điểm toán: "))
#     chiTiet["Tiếng việt"] = float(input("Điểm tiếng việt: "))
#     chiTiet["TB"] = (chiTiet["Toán"] + chiTiet["Tiếng việt"]) / 2
#     chiTiet["Xếp loại"] = xepLoai(chiTiet["TB"])
#     danhSach.append(chiTiet)

# print("Họ tên \tĐiểm toán\tĐiểm tiếng việt\tĐiểm trung bình\tXếp loại")
# for i in danhSach:
#     print(i["Tên học sinh"],"\t",i["Toán"],"\t",i["Tiếng việt"],"\t",i["TB"],"\t",i["Xếp loại"])


# Bài toán
# def timUoc(num):
#     uoc = []
#     for i in range(1,num+1):
#         if (num % i == 0):
#             uoc.append(i)
#     return uoc
# print("Số nguyên tố dưới 100: ")
# for i in range(1,101):
#     if (len(timUoc(i)) <= 2): print(i)


# n = 1
# dsSV = []
# while(n == 1):
#     while(True):
#         try:
#             sbd = int(input("Nhập số báo danh (5 số): "))
#             if (len(str(sbd)) == 5): break
#         except:
#             print("Lỗi nhập liệu!")

#     while(True):
#         hoten = input("Họ và tên (Không quá 25 ký tự): ")
#         if (len(hoten) <= 25): break

#     while(True):
#         try:
#             diemToan = float(input("Nhập điểm toán (Từ 0 đến 10): "))
#             if (diemToan >= 0 and diemToan <= 10): break
#         except:
#             print("Lỗi nhập liệu!")

#     while(True):
#         try:
#             diemTiengViet = float(input("Nhập điểm tiếng việt (Từ 0 đến 10): "))
#             if (diemTiengViet >= 0 and diemTiengViet <= 10): break
#         except:
#             print("Lỗi nhập liệu!")
    
#     dsSV.append({"Số báo danh": sbd, "Họ tên": hoten, "Điểm toán": diemToan, "Điểm tiếng việt": diemTiengViet})

#     try:
#         n = int(input("Nhập 1 để nhập thí sinh, 2 để kết thúc nhập: "))
#     except:
#         n = 0
# else:
#     print("Kết thúc nhập!")

# print("Danh sách sinh viên đã nhập liệu")
# for ds in dsSV:
#     print("Số báo danh\t\tHọ tên\t\tĐiểm toán\t\tĐiểm tiếng việt")
#     print(ds["Số báo danh"],"\t\t",ds["Họ tên"],"\t\t",ds["Điểm toán"],"\t\t",ds["Điểm tiếng việt"])

# print("Danh sách sinh viên có tổng điểm > 10")
# for ds in dsSV:
#     if (ds["Điểm toán"] + ds["Điểm tiếng việt"] > 10):
#         print(ds["Số báo danh"],"\t\t",ds["Họ tên"],"\t\t",ds["Điểm toán"],"\t\t",ds["Điểm tiếng việt"])

# print("Danh sách sinh viên có điểm liệt")
# for ds in dsSV:
#     if (ds["Điểm toán"] == 0 or ds["Điểm tiếng việt"] == 0):
#         print(ds["Số báo danh"],"\t\t",ds["Họ tên"],"\t\t",ds["Điểm toán"],"\t\t",ds["Điểm tiếng việt"])

# Bài toán
# def tinhTienDien(kwDien):
#     if (kwDien <= 100): return 1450*kwDien + (1450*kwDien*10/100)
#     elif (kwDien > 100 and kwDien <= 150): return 1750*kwDien + (1750*kwDien*10/100)
#     elif (kwDien > 150 and kwDien <= 250): return 2000*kwDien + (2000*kwDien*10/100)
#     else: return 2500*kwDien + (2500*kwDien*10/100)

# def ghiFile(toaNha,thongTin):
#     ghi = open(toaNha + ".txt",mode="a",encoding="utf-8")
#     ghi.write(thongTin + "\n")
#     ghi.close()

# electric = open("electric.txt",mode="w",encoding="utf-8")
# n = 1
# chungCu = []
# while(True):
#     try:
#         n = int(input("Nhap 1 de nhap thong tin, nhap ky tu khac de thoat: "))
#         if (n != 1): break
#         while(True):
#             sohieuphong = input("Nhap so hieu phong: ")
#             if (sohieuphong != ""): break

#         while(True):
#             sohieutoanha = input("Nhap so hieu toa nha: ")
#             if (sohieutoanha != ""): break
            
#         while(True):
#             tenchuho = input("Nhap ten chu ho: ")
#             if (tenchuho != ""): break

#         while(True):
#             try:                
#                 dientieuthu = int(input("So dien thieu thu trong thang (>=0): "))
#                 if (dientieuthu >=0): break
#             except:
#                 print("")
        
#         giaTien = tinhTienDien(dientieuthu)
#         chungCu.append({"PHONG": sohieuphong, "TOANHA": sohieutoanha, "CHUHO": tenchuho, "DIENTIEUTHU": dientieuthu, "TIENDIEN": "{:,}".format(int(giaTien))})
#         ghiFile(sohieutoanha, sohieuphong + "\t" + tenchuho + "\t" + str(dientieuthu) + "\t" + "{:,}".format(int(giaTien)))
#     except:
#         break
# print("DANH SACH SU DUNG DIEN TAI CHUNG CU")
# print("TOANHA\t\tPHONG\t\tSODIENTIEUTHU\t\tTIENDIENPHAITRA")
# for ds in chungCu:
#     print(ds["TOANHA"],"\t\t",ds["PHONG"],"\t\t",ds["DIENTIEUTHU"],"\t\t",ds["TIENDIEN"])
# electric.close()


# Thực hành với class
# class MonHoc():
#     def __init__(self, maMH = "", tenMH = "", soTiet = ""):
#         self.__maMH = maMH
#         self.__tenMH = tenMH
#         self.__soTiet = soTiet

#     def nhapMH(self):
#         self.__maMH = input("Mã môn học: ")
#         self.__tenMH = input("Tên môn học: ")
#         self.__soTiet = input("Số tiết: ")

#     def thongTin(self):
#         # print("Mã môn      Tên môn       Số tiết")
#         print(self.__maMH,"\t",self.__tenMH,"\t",self.__soTiet)

    
# class HocVien():
#     def __init__(self,cccd,ten,namsinh):
#         self.__cccd = cccd
#         self.__ten = ten
#         self.__namsinh = namsinh
#         self.__monHoc = []
    
#     def thongTinHocVien(self):
#         print(self.__cccd,"\t",self.__ten,"\t",self.__namsinh)

#     def dangKyMonHoc(self):
#         mon = MonHoc()
#         mon.nhapMH()
#         self.__monHoc.append(mon)

#     def thongTinMonHoc(self):
#         print("Mã môn      Tên môn       Số tiết")
#         for mh in self.__monHoc:
#             mh.thongTin()
    
#     def soMonDangKy(self):
#         return len(self.__monHoc)

#     def checkDangKy(self):
#         if (len(self.__monHoc) >= 2):
#             return True
#         else:
#             return False
# # Khởi tạo danh sách môn học
# monToan = MonHoc("TOAN","Môn Toán",10)
# monLy = MonHoc("LY","Môn Lý",10)
# monHoa = MonHoc("HOA","Môn Hoá",10)

# # Khởi tạo dữ liệu học viên
# hocVien = list()
# n = 1
# while(n == 1):
#     try:
#         n = int(input("Press 1 to input, other to cancel: "))
#         if (n != 1): break
#     except:
#         break

#     while(True):
#         cccd = input("Input CCCD: ")
#         if (cccd != ""): break
#     while(True):
#         ten = input("Input name: ")
#         if (ten != ""): break
    
#     while(True):
#         try:
#             tuoi = int(input("Input age: "))
#             break
#         except:
#             print("") #nothing
#     hv = HocVien(cccd,ten,tuoi)
#     hocVien.append(hv)  
#     x = 1
#     while(x == 1):
#         try:
#             x = int(input("What subject you choose?\nPress 1 to input, other to end: "))
#             if (x != 1): break
#         except:
#             break
#         temp = hocVien[int(len(hocVien) - 1)]
#         temp.dangKyMonHoc()  

# print("Thông tin học viên đăng ký ít nhất 02 môn")
# for hs in hocVien:
#     if (hs.checkDangKy() == True):
#         hs.thongTinHocVien()
#         hs.thongTinMonHoc()

