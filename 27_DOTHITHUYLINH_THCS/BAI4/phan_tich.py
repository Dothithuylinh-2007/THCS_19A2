from du_lieu.danh_sach import sap_xep
from du_lieu.tu_dien import lay_gia_tri
ds = list(map(int, input("Nhập danh sách số (cách nhau bởi khoảng trắng): ").split()))
khoa = input("Nhập khóa cần lấy giá trị: ")
td = {}
for i in range(len(ds)):
    td[str(i)] = ds[i]
print("Danh sách sau khi sắp xếp:", sap_xep(ds))
print("Giá trị theo khóa:", lay_gia_tri(td, khoa))