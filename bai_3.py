def CalculateVND(no_kwh: int) -> int:
    total_money: int
    if no_kwh <= 50:
        total_money = no_kwh * 1600
    elif no_kwh <= 100:
        no_kwh -= 50
        total_money = 50 * 1600 + no_kwh * 2000
    else:
        no_kwh -= 100
        total_money = 50 * 1600 + 50 * 2000 + no_kwh * 2500
    return total_money


if "__main__" == __name__:
    try:
        nokwh = int(input("Nhap so kwh: "))
    except TypeError:
        print("Sai kieu du lieu")

    totalmoney = CalculateVND(nokwh)
