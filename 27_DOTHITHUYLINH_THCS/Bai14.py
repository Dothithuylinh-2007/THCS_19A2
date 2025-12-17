n = int(input("Nhập số phần tử của A: "))
list_A = [0] * n
for i in range(n):
    list_A[i] = int(input())
A = set(list_A)
m = int(input("Nhập số phần tử của B: "))
list_B = [0] * m
for i in range(m):
    list_B[i] = int(input())
B = set(list_B)
print("A - B:", A - B)
print("B - A:", B - A)
print("Giao:", A & B)
print("Hợp:", A | B)