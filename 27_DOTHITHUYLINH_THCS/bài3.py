tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
a = tu
if a < 0:
    a = -a
b = mau
if b < 0:
    b = -b
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
ucln = a        
tu = tu // ucln
mau = mau // ucln
if mau < 0:
    tu = -tu
    mau = -mau
print("Phân số tối giản:", tu, "/", mau)