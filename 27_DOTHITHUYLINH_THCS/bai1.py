gia = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))
tong_chi_phi = gia * so_luong
vat = tong_chi_phi * 0.10
tong_phai_tra = tong_chi_phi + vat
print(f"Tổng tiền phải trả là: {tong_phai_tra:.2f} VND")