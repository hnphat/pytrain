class MonHoc():
    def __init__(self, maMH = "", tenMH = "", soTiet = ""):
        self.__maMH = maMH
        self.__tenMH = tenMH
        self.__soTiet = soTiet

    def nhapMH(self):
        self.__maMH = input("Mã môn học: ")
        self.__tenMH = input("Tên môn học: ")
        self.__soTiet = input("Số tiết: ")

    def thongTin(self):
        # print("Mã môn      Tên môn       Số tiết")
        print(self.__maMH,"\t",self.__tenMH,"\t",self.__soTiet)

    
class HocVien():
    def __init__(self,cccd,ten,namsinh):
        self.__cccd = cccd
        self.__ten = ten
        self.__namsinh = namsinh
        self.__monHoc = []
    
    def thongTinHocVien(self):
        print(self.__cccd,"\t",self.__ten,"\t",self.__namsinh)

    def dangKyMonHoc(self):
        mon = MonHoc()
        mon.nhapMH()
        self.__monHoc.append(mon)

    def thongTinMonHoc(self):
        print("Mã môn      Tên môn       Số tiết")
        for mh in self.__monHoc:
            mh.thongTin()
    
    def soMonDangKy(self):
        return len(self.__monHoc)

    def checkDangKy(self):
        if (len(self.__monHoc) >= 2):
            return True
        else:
            return False
# Khởi tạo danh sách môn học
monToan = MonHoc("TOAN","Môn Toán",10)
monLy = MonHoc("LY","Môn Lý",10)
monHoa = MonHoc("HOA","Môn Hoá",10)

# Khởi tạo dữ liệu học viên
hocVien = list()
n = 1
while(n == 1):
    try:
        n = int(input("Press 1 to input, other to cancel: "))
        if (n != 1): break
    except:
        break

    while(True):
        cccd = input("Input CCCD: ")
        if (cccd != ""): break
    while(True):
        ten = input("Input name: ")
        if (ten != ""): break
    
    while(True):
        try:
            tuoi = int(input("Input age: "))
            break
        except:
            print("") #nothing
    hv = HocVien(cccd,ten,tuoi)
    hocVien.append(hv)  
    x = 1
    while(x == 1):
        try:
            x = int(input("What subject you choose?\nPress 1 to input, other to end: "))
            if (x != 1): break
        except:
            break
        temp = hocVien[int(len(hocVien) - 1)]
        temp.dangKyMonHoc()  

print("Thông tin học viên đăng ký ít nhất 02 môn")
for hs in hocVien:
    if (hs.checkDangKy() == True):
        hs.thongTinHocVien()
        hs.thongTinMonHoc()

