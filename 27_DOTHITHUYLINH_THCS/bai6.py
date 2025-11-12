nam = int(input("Nhập năm: "))
nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
print(f"Năm {nam} là năm nhuận: {nam_nhuan}")