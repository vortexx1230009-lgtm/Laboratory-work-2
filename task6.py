def average(*numbers):
    return sum(numbers) / (len(numbers) or 1)
values = input("Qiymətləri boşluqlar ilə daxil edin (məsələn: 70 80 90): ")
numbers = [float(x) for x in values.split()]
print("Ortalama:", average(*numbers))
