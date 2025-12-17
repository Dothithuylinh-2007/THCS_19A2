n = int(input("Nhập số phần tử: "))
a = [0] * n
for i in range(n):
    a[i] = int(input())
b = [0] * n
dem = 0
for i in range(n):
    trung = False
    for j in range(dem):
        if a[i] == b[j]:
            trung = True
            break
    if trung == False:
        b[dem] = a[i]
        dem = dem + 1
for i in range(dem):
    print(b[i], end=" ")