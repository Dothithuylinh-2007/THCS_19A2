can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))
bmi = can_nang / (chieu_cao ** 2)
print(f"Chỉ số BMI = {bmi:.2f}")