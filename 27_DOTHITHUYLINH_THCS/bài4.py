n = int(input("Nhập n: "))
print("Các số nguyên tố nhỏ hơn", n, "là:")
x = 2
while x < n:
    dem = 0
    i = 1
    while i <= x:
        if x % i == 0:
            dem = dem + 1
        i = i + 1
    if dem == 2:
        print(x) 
    x = x + 1