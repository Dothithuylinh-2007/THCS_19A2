n = int(input("Nhập số phần tử: "))
a = [0] * n
for i in range(n):
    a[i] = int(input())
k = int(input("Nhập k: "))
k = k % n
for t in range(k):
    cuoi = a[n - 1]
    i = n - 1
    while i > 0:
        a[i] = a[i - 1]
        i = i - 1
    a[0] = cuoi
for i in range(n):
    print(a[i], end=" ")