tien_gui = float(input("Nhập số tiền gửi: "))
lai_suat = float(input("Nhập lãi suất hàng năm (%): "))
lai_1_thang = tien_gui * (lai_suat / 100) * (1/12)
lai_2_quy = tien_gui * (lai_suat / 100) * (2/4)
lai_3_nam = tien_gui * (lai_suat / 100) * 3
print(f"Lãi 1 tháng: {lai_1_thang:.2f}, 2 quý: {lai_2_quy:.2f}, 3 năm: {lai_3_nam:.2f}")