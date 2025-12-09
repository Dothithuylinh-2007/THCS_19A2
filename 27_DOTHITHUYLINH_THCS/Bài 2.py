def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0 and b == 0:
        return "Phương trình có vô số nghiệm"
    elif a == 0:
        return "Phương trình vô nghiệm"
    else:
        return f"Nghiệm x = {-b / a}"
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print(giai_phuong_trinh_bac_nhat(a, b))