from may_tinh.co_ban import cong, tru
from may_tinh.nang_cao import luy_thua, can_bac_hai
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
co_so = float(input("Nhập cơ số: "))
so_mu = float(input("Nhập số mũ: "))
so = float(input("Nhập số cần căn bậc hai: "))
print("Tổng:", cong(a, b))
print("Hiệu:", tru(a, b))
print("Lũy thừa:", luy_thua(co_so, so_mu))
print("Căn bậc hai:", can_bac_hai(so))