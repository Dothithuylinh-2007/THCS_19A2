def tim_so_le_lon_nhat(a, b, c):
    max_le = -1
    for x in (a, b, c):
        if x % 2 != 0 and x > max_le:
            max_le = x
    return max_le
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
kq = tim_so_le_lon_nhat(a, b, c)
if kq == -1:
    print("Không có số lẻ.")
else:
    print("Số lẻ lớn nhất là:", kq)