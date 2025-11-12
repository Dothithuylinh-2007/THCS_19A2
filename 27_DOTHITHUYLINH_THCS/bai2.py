tong_keo = int(input("Nhập tổng số kẹo: "))
so_hs = int(input("Nhập số học sinh: "))
moi_hs = tong_keo // so_hs
con_thua = tong_keo % so_hs
print(f"Mỗi học sinh nhận {moi_hs} kẹo, còn thừa {con_thua} kẹo")