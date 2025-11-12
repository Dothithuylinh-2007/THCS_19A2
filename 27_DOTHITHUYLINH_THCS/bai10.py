luong_co_ban = float(input("Nhập mức lương cơ bản: "))
ngay_cong = float(input("Nhập số ngày công trong tháng: "))
luong_ngay = luong_co_ban / 22
luong_thuc_nhan = luong_ngay * ngay_cong
luong_thuc_nhan += luong_thuc_nhan * 0.10 * (ngay_cong > 22)
luong_thuc_nhan -= luong_thuc_nhan * 0.05 * (ngay_cong < 22)
print(f"Tổng tiền lương thực nhận: {luong_thuc_nhan:.2f} VNĐ")