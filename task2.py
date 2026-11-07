price = float(input("Məhsulun Qiymətini daxil edin: "))
def add_vat(price, vat_percent=18):
    return price + (price * vat_percent / 100)
print("ƏDV daxil məhsulun qiymət:", add_vat(price))
print(add_vat(50,10))
print(add_vat(vat_percent=5, price=80))
