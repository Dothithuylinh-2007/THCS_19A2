with open("nguon.bin", "rb") as f_nguon:
    with open("dich.bin", "wb") as f_dich:
        while True:
            du_lieu = f_nguon.read(1024)
            if not du_lieu:
                break
            f_dich.write(du_lieu)
print("Sao chép file hoàn tất.")