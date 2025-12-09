def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập số n: "))
if la_so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")
def in_so_nguyen_to_trong_khoang(a, b):
    print(f"Các số nguyên tố trong đoạn [{a}, {b}] là:")
    for x in range(a, b + 1):
        if la_so_nguyen_to(x):
            print(x, end=" ")
print() 
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
in_so_nguyen_to_trong_khoang(a, b)