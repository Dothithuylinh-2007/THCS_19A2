username = input("Nhập tên đăng nhập: ")
password = input("Nhập mật khẩu: ")
quyen_truy_cap = (username == "admin") and (password != "password123")
print(f"Được quyền truy cập: {quyen_truy_cap}")