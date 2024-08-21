def checkMail(mail):
    if (mail.find("@") < 0 or mail.count("@") > 1):
        print("Email không hợp lệ")
    else:
        str = mail.split("@")
        if (str[0] == "" or str[1] == ""): print("Địa chỉ và tên miền không được trống")
        elif (str[1].find(".") < 0 or str[1].count(".") > 1): print("tên miền email không hợp lệ")
        else: print("Email hợp lệ")
