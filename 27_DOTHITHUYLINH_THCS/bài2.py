a = int(input("nhập a: "))
b = int(input("nhập b: "))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print("UCLN= ", a)