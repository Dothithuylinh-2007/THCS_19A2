kwh = float(input("Nhập số kWh điện đã tiêu thụ: "))
tien_dien = (kwh * 1678) * (kwh <= 100) + \
         (100 * 1678 + (kwh - 100) * 1734) * (100 < kwh <= 200) + \
            (100 * 1678 + 100 * 1734 + (kwh - 200) * 2014) * (kwh > 200)
print(f"Tổng tiền điện phải trả: {tien_dien:.2f} VNĐ")