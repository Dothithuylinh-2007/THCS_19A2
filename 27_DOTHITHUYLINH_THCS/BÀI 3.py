ds_so = [1, 5, 10, 20, 50]
with open("so_nguyen.txt", "w", encoding="utf-8") as f:
    for so in ds_so:
        f.write(str(so) + "\n")