n = int(input("nhập vào só n: "))
i = 1
while i*i < n:
    i = i + 1
if i*i == n:
    print("số chính phương")
else:
    print("không là số chính phương")