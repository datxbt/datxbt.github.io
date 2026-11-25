kw = int(input("Nhap so KW: "))
ngheo = int(input("Ho ngheo? (1: co, 0: khong): "))

gia2 = 600
if ngheo == 1:
    gia2 = 450

if kw <= 100:
    tien = kw * 450
elif kw <= 200:
    tien = 100 * 450 + (kw - 100) * gia2
elif kw <= 300:
    tien = 100 * 450 + 100 * gia2 + (kw - 200) * 750
elif kw <= 500:
    tien = 100 * 450 + 100 * gia2 + 100 * 750 + (kw - 300) * 900
elif kw <= 1000:
    tien = 100 * 450 + 100 * gia2 + 100 * 750 + 200 * 900 + (kw - 500) * 1000
else:
    tien = 100 * 450 + 100 * gia2 + 100 * 750 + 200 * 900 + 500 * 1000 + (kw - 1000) * 1200

vat = tien * 0.1
phi = tien * 0.02

print("Tien truoc thue:", tien)
print("Tien sau thue VAT:", tien + vat)
print("Phi bao ve moi truong:", phi)
print("Tong phai nop:", tien + vat + phi)
