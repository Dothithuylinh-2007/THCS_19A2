from thu_vien_chung.xu_ly_so import la_so_nguyen_to
n = int(input("Nhập số cần kiểm tra: "))
if la_so_nguyen_to(n):
    print("Đây là số nguyên tố")
else:
    print("Đây không phải số nguyên tố")