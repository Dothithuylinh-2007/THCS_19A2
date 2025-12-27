with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write("1,Laptop,1200\n")
    f.write("2,Chuot may tinh,25\n")
    f.write("3,Ban phim,75\n")
id_can_sua = input("Nhap ID san pham: ")
gia_moi = input("Nhap gia moi: ")
ds = []
with open("san_pham.txt", "r", encoding="utf-8") as f:
    for dong in f:
        tach = dong.strip().split(",")
        if tach[0] == id_can_sua:
            tach[2] = gia_moi
            dong = ",".join(tach) + "\n"
        ds.append(dong)
with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.writelines(ds)
print("Da cap nhat gia san pham!")