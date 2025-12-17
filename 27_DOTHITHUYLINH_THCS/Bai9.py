n = int(input("Nhập n: "))
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())
tong = 0
for i in range(n):
    tong = tong + a[i][n - i - 1]
print("Tổng:", tong)