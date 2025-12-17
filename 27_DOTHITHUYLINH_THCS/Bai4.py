n = int(input("Nhập số phần tử: "))
a = [0] * n
for i in range(n):
    a[i] = int(input())
max1 = a[0]
for i in range(n):
    if a[i] > max1:
        max1 = a[i]
max2 = None
for i in range(n):
    if a[i] != max1:
        if max2 is None or a[i] > max2:
            max2 = a[i]
print("Số lớn thứ hai:", max2)