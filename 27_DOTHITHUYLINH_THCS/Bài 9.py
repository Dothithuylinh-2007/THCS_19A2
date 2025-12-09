def tong_chu_so(n):
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong
n = int(input("Nhập n: "))
print(tong_chu_so(n))