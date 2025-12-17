n = int(input("Nhập n: "))
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())
la_don_vi = True
for i in range(n):
    for j in range(n):
        if i == j:
            if a[i][j] != 1:
                la_don_vi = False
        else:
            if a[i][j] != 0:
                la_don_vi = False
if la_don_vi:
    print("Ma trận đơn vị")
else:
    print("Không phải ma trận đơn vị")