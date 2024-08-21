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
        elif (str[1].find(".") < 0 or str[1].count(".") > 1): print("tên miền email không hợp lệ")
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



