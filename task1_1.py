def print_student_card(name, group, year):
    print(f"Name: {name}\nGroup: {group}\nYear: {year}")
name = input("Adınızı daxil edin: ")
group = input("Qrupunuzu daxil edin: ")
year = input("Neçənci kurs olduğunuzu daxil edin: ")
print_student_card(name, group, year)
print_student_card("Aysel Mammadova", "CE-101", 1)
print_student_card(year=2, name="Kamran Aliyev", group="CE-201")
