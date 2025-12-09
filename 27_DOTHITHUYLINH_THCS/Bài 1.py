def chuyen_doi_nhiet_do(do_c):
    return do_c * 9/5 + 32
do_c = float(input("Nhập nhiệt độ C: "))
print("Độ F =", chuyen_doi_nhiet_do(do_c))