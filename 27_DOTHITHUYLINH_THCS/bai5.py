n = int(input("Nhập n: "))
S1 = 0
i = 1
while i <= n:
    S1 = S1 + i
    i = i + 1
S2 = 1
i = 1
while i < n:
    S2 = S2 * i
    i = i + 1
S3 = 0
i = 1
while i <= n:
    S3 = S3 + ((-1)**(i + 1)) * (1 / i)
    i = i + 1
S4 = 0
k = 0
while k <= n:
    S4 = S4 + (k / (k + 2))
    k = k + 1
print(f"S1 = {S1}, S2 = {S2}, S3 = {S3}, S4 = {S4}")