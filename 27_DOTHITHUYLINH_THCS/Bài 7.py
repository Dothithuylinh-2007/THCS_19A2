def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
def tinh_tong_hoan_hao(a, b):
    tong = 0
    for n in range(a, b + 1):
        if la_so_hoan_hao(n):
            tong += n
    return tong
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print(tinh_tong_hoan_hao(a, b))