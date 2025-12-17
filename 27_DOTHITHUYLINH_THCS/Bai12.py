m = int(input("Hàng A: "))
n = int(input("Cột A = hàng B: "))
p = int(input("Cột B: "))
A = [[0]*n for i in range(m)]
B = [[0]*p for i in range(n)]
C = [[0]*p for i in range(m)]
for i in range(m):
    for j in range(n):
        A[i][j] = int(input())
for i in range(n):
    for j in range(p):
        B[i][j] = int(input())
for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]
for i in range(m):
    for j in range(p):
        print(C[i][j], end=" ")
    print()