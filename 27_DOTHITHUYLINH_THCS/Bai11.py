n = int(input("Nhập n: "))
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())
doi_xung = True
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            doi_xung = False
if doi_xung:
    print("Ma trận đối xứng")
else:
    print("Không đối xứng")