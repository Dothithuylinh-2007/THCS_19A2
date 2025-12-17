n = int(input("Nhập số phần tử: "))
t = ()
for i in range(n):
    t = t + (int(input()),)
chan = ()
le = ()
tong_chan = 0
tong_le = 0
for x in t:
    if x % 2 == 0:
        chan = chan + (x,)
        tong_chan = tong_chan + x
    else:
        le = le + (x,)
        tong_le = tong_le + x
print("Tuple chẵn:", chan)
print("Tuple lẻ:", le)
print("Tổng chẵn:", tong_chan)
print("Tổng lẻ:", tong_le)