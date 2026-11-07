def build_username(first, last, year=""):
    username = f"{first}.{last}".lower()
    if year:
        username += str(year)
    return username
first = input("Adınızı daxil edin: ")
last = input("Soyadınızı daxil edin: ")
year = input("İl və ya rəqəm daxil edin (boş buraxa bilərsiniz): ")
print("İstifadəçi adı:", build_username(first, last, year))
print(build_username("Aysel", "Mammadova"))
print(build_username("Kamran", "Aliyev", 2005))
