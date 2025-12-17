s = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))
tu = ""
do_dai = 0
for ky_tu in s + " ":
    if ky_tu != " ":
        tu += ky_tu
        do_dai += 1
    else:
        if do_dai > n:
            print(tu)
        tu = ""
        do_dai = 0