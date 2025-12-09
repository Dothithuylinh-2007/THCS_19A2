def kiem_tra_so_doi_xung(n):
    s = str(n)
    return s == s[::-1]
n = int(input("Nhập n: "))
print(kiem_tra_so_doi_xung(n))