with open("vanban.txt", "w", encoding="utf-8") as f:
    f.write("Python là một ngôn ngữ lập trình mạnh mẽ, dễ học và có nhiều ứng dụng.")
with open("vanban.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
so_tu = len(noi_dung.split())
print("Nội dung file:")
print(noi_dung)
print("Số từ trong file:", so_tu)