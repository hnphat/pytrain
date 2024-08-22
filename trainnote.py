def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n > 1: return fibo(n-1) + fibo(n-2)
    else: return "n <= 1"

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

set1 = {1,2,3,4,5,"ABC",2.5,(1,2),True} # Không sử dụng list trong set

list1 = [1,2,3,4,5,(1,2),{"a":1},True]
tuple1 = (1,2,3,4,5, (1,2), [1,2], {"A":1},True)

dict1 = dict({"A": "Apple", "A": "Apple", "C": [1,2,3], "D": (1,2,3,4), "E": {1,2,3,4,5}, "F": 2.5, "G": dict({"A":1}), "H": True})

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