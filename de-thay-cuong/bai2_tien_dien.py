# Bài 2 (4 điểm): Tính tiền điện theo bậc thang
#   1 - 100   : 450 đ/kW   (hộ nghèo: 1 - 200 đều 450 đ/kW)
#   101 - 200 : 600 đ/kW
#   201 - 300 : 750 đ/kW
#   301 - 500 : 900 đ/kW
#   501 - 1000: 1000 đ/kW
#   trên 1000 : 1200 đ/kW
# VAT = 10% tiền điện; phí bảo vệ môi trường = 2% tiền điện (tính trên tiền trước thuế)


def tinh_tien_dien(kw, ho_ngheo):
    # Mỗi bậc gồm (mốc trên của bậc, giá). Bậc cuối không có mốc trên nên để số rất lớn.
    if ho_ngheo == 1:
        bac = [(200, 450), (300, 750), (500, 900), (1000, 1000), (10**12, 1200)]
    else:
        bac = [(100, 450), (200, 600), (300, 750), (500, 900), (1000, 1000), (10**12, 1200)]

    tien = 0
    moc_truoc = 0
    for moc, gia in bac:
        if kw > moc:
            tien = tien + (moc - moc_truoc) * gia      # dùng hết bậc này
            moc_truoc = moc
        else:
            tien = tien + (kw - moc_truoc) * gia       # dừng ở bậc này
            break
    return tien


def nhap_so_kw():
    while True:
        try:
            kw = float(input("Nhập số kW tiêu thụ: "))
            if kw < 0:
                print("Số kW không được âm, nhập lại!")
            else:
                return kw
        except ValueError:
            print("Phải nhập số, nhập lại!")


def nhap_ho_ngheo():
    while True:
        s = input("Có phải hộ nghèo không? (1: Hộ nghèo, 0: Không nghèo): ").strip()
        if s == "0" or s == "1":
            return int(s)
        print("Chỉ được nhập 0 hoặc 1, nhập lại!")


def main():
    kw = nhap_so_kw()
    ho_ngheo = nhap_ho_ngheo()

    tien_dien = tinh_tien_dien(kw, ho_ngheo)
    vat = tien_dien * 0.10
    phi_mt = tien_dien * 0.02
    tong = tien_dien + vat + phi_mt

    print("--------------------------------------------")
    print(f"Số kW tiêu thụ              : {kw:g}")
    if ho_ngheo == 1:
        print("Loại hộ                     : Hộ nghèo")
    else:
        print("Loại hộ                     : Không nghèo")
    print(f"Tiền điện (trước thuế)      : {tien_dien:,.0f} đ")
    print(f"Thuế VAT 10%                : {vat:,.0f} đ")
    print(f"Tiền sau thuế VAT           : {tien_dien + vat:,.0f} đ")
    print(f"Phí bảo vệ môi trường 2%    : {phi_mt:,.0f} đ")
    print(f"TỔNG PHẢI NỘP               : {tong:,.0f} đ")


if __name__ == "__main__":
    main()
