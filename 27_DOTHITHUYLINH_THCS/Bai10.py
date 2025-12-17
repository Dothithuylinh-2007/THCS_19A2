m = int(input("Số hàng: "))
n = int(input("Số cột: "))
a = [[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = int(input())
max_tong = None
hang_max = 0
for i in range(m):
    tong = 0
    for j in range(n):
        tong = tong + a[i][j]
    if max_tong is None or tong > max_tong:
        max_tong = tong
        hang_max = i
print("Hàng có tổng lớn nhất:", hang_max)