Laboratoriya işi № 8: Funksiyalar (Functions)

Fənn: Fundamentals of Programming 1

Tələbə: İsmət Qurbanov

Qovluq adı: lab8_Ismat_Gurbanov

1. Layihə Qovluğunun Strukturu

Kompüterinizdə lab8_Ismat_Gurbanov qovluğu yaradın və bütün faylları həmin qovluğun daxilində saxlayın:

lab8_Ismat_Gurbanov/
├── utils.py
├── lab8_main.py
├── task8_fixed.py
├── bonus_journal.py
├── report_en.docx (və ya report.txt)
└── README.md


2. Faylların Tam Kodları

📄 utils.py

(Tapşırıq 2, 3, 5 və 6-dakı köməkçi funksiyalar modulu)

"""Laboratoriya 8 üçün köməkçi funksiyalar modulu."""


def add_vat(price, vat_percent=18):
    """Qiymətə ƏDV əlavə edib yeni qiyməti qaytarır."""
    return price + (price * vat_percent / 100)


def build_username(first, last, year=""):
    """first.last formatında kiçik hərflərlə istifadəçi adı qaytarır."""
    username = first.lower() + "." + last.lower()
    if year:
        username += str(year)
    return username


def add_bonus(scores, bonus):
    """Hər balı bonus qədər yerində artırır (maksimum 100)."""
    for i in range(len(scores)):
        scores[i] = min(100, scores[i] + bonus)


def with_bonus(scores, bonus):
    """Bonus əlavə edilmiş yeni siyahı qaytarır, orijinalı dəyişmir."""
    new_scores = []
    for score in scores:
        new_scores.append(min(100, score + bonus))
    return new_scores


def average(*numbers):
    """Verilən ədədlərin ədədi ortasını qaytarır."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def make_course(code, **details):
    """Kurs kodu və detallardan ibarət dictionary qaytarır."""
    course = {"code": code}
    for key, value in details.items():
        course[key] = value
    return course


📄 lab8_main.py

(Tapşırıq 1, 4, 5, 6 və 7-nin icra kodu)

"""Laboratoriya 8 əsas icra faylı."""

import utils
from utils import average
from utils import build_username as make_user
import utils as u


# --- Tapşırıq 1: print_student_card ---
def print_student_card(name, group, year):
    """Tələbə kartı məlumatlarını çap edir."""
    print("Name:", name)
    print("Group:", group)
    print("Year:", year)


# 1. Mövqeli arqumentlərlə çağırış
print_student_card("Aysel Mammadova", "CE-101", 1)

# 2. Açar sözlü arqumentlərlə çağırış
print_student_card(year=2, name="Kamran Aliyev", group="CE-201")

# 3. İki arqumentli çağırış (xəta verir, şərhə çevrildi):
# print_student_card("Aysel Mammadova", "CE-101")


# --- Tapşırıq 4: make_student və while dövrü ---
def make_student(name, score, group=""):
    """Tələbə lüğətini formalaşdırıb qaytarır."""
    student = {"name": name, "score": score}
    if group:
        student["group"] = group
    return student


print(make_student("Kamran", 61, "CE-101"))

students = []
while True:
    name_input = input("Name (quit to stop): ")
    if name_input.lower() == "quit":
        break
    score_input = int(input("Score: "))
    students.append(make_student(name_input, score_input))

for s in students:
    print(s["name"] + ": " + str(s["score"]))


# --- Tapşırıq 5: Listlərin funksiyaya ötürülməsi yoxlanışı ---
scores = [70, 95, 88, 100]
print(u.with_bonus(scores, 10))
print(scores)
utils.add_bonus(scores[:], 10)
print(scores)
utils.add_bonus(scores, 10)
print(scores)


# --- Tapşırıq 6 və 7: Modul importları və *args, **kwargs yoxlanışı ---
print(utils.add_vat(200))
print(average(60, 70))
print(make_user("Nigar", "Hasanova"))
print(u.with_bonus([50, 95], 10))


📄 task8_fixed.py

(Tapşırıq 8: 4 xətası düzəldilmiş kod)

"""Düzəldilmiş Tapşırıq 8 kodu."""


def calculate_total(prices, discount=0):
    total = 0
    for price in prices:
        total += price
    total = total - total * discount / 100
    return total


def describe_order(city, customer, country="Azerbaijan"):
    return customer + " ordered from " + city + ", " + country


order_total = calculate_total([10, 20, 30], 10)
print("Total: " + str(order_total))
print(describe_order("Baku", customer="Ali"))


📄 bonus_journal.py

(Bonus Tapşırıq: Tələbə jurnalı v2)

"""Bonus: Tələbə Jurnalı v2."""


def make_student(name, score):
    return {"name": name, "score": score}


def add_student(students, name, score):
    students.append(make_student(name, score))


def average_score(students):
    if not students:
        return 0
    total = sum(s["score"] for s in students)
    return total / len(students)


def top_student(students):
    if not students:
        return None
    top = students[0]
    for s in students:
        if s["score"] > top["score"]:
            top = s
    return top


def print_report(students):
    for s in students:
        print(s["name"] + ": " + str(s["score"]))
    print("Average:", average_score(students))
    best = top_student(students)
    if best:
        print("Top student: " + best["name"] + " (" + str(best["score"]) + ")")


students = []
while True:
    choice = input("Choice: ")
    if choice == "1":
        name = input("Name: ")
        score = int(input("Score: "))
        add_student(students, name, score)
    elif choice == "2":
        print_report(students)
    elif choice == "3":
        break
    else:
        print("Yanlış seçim!")


3. Hesabat Mətni (Report - English A2)

Part A: Predict first, then run (10 points)

A1 Code Prediction:

Salam, Aysel!
Xosh gəldin, Kamran!
Sabahınız xeyir, Nigar!


A2 Code Prediction:

16
16
None


Question: Why does b get this value? What is the main difference between square and show_square?

Answer: square() uses return to send back the result, so variable a gets 16. show_square() only prints the value to the screen and does not return anything. In Python, when a function does not have a return statement, it returns None. Therefore, b is None.

A3 Code Prediction:

['bread', 'milk']
['bread', 'milk', 'cheese']


Explanation: add_item() modifies the original list directly using append(). add_item_copy() creates a new copy of the list with items[:] and adds the item only to that copy. Thus, the original basket list does not change.

Task 1: Error Explanation (10 points)

Error message: TypeError: print_student_card() missing 1 required positional argument: 'year'

Explanation: The function requires 3 positional arguments, but only 2 were given, so Python raises a TypeError.

Task 2: Default Arguments (10 points)

Question: Why must a parameter with a default value be placed after parameters without a default value?

Answer: Python matches positional arguments from left to right. If a default parameter is placed first, Python cannot determine which argument belongs to which parameter. This results in a SyntaxError.

Task 5: Passing Lists (15 points)

Question: Explain why each line gives this output in 3–4 sentences. What does scores[:] do?

Answer:

with_bonus(scores, 10) creates and returns a new list, leaving the original scores unchanged as [70, 95, 88, 100].

scores[:] makes a shallow copy of the list. add_bonus(scores[:], 10) modifies only this copy, leaving scores still as [70, 95, 88, 100].

add_bonus(scores, 10) modifies the original list directly in place, updating it to [80, 100, 98, 100].

Task 7: Module Imports (10 points)

Question: Why is it not recommended to write from utils import *?

Answer: It imports all functions and variables into the current namespace, which can overwrite existing names and cause conflicts. It also makes the code harder to read because it is unclear where each function comes from.

Task 8: Bug Fix Table (10 points)

№

Error Type

Location

How it was fixed

1

SyntaxError

calculate_total header (discount=0)

Added a colon (:) at the end of the def line.

2

Logical error / TypeError

End of calculate_total function

Replaced print(total) with return total so the function returns the value instead of None.

3

SyntaxError

describe_order parameter list

Moved city before country="Azerbaijan" because non-default parameters must come before default parameters.

4

TypeError

describe_order call

Adjusted the call to describe_order("Baku", customer="Ali") to match the corrected parameter order.

4. GitHub README.md Faylı

# Fundamentals of Programming 1 - Lab 8: Functions

This repository contains my laboratory solutions for **Functions in Python**, based on Chapter 8 of *Python Crash Course*.

## 📁 Repository Structure

```text
lab8_Ismat_Gurbanov/
├── utils.py           # Reusable helper functions
├── lab8_main.py       # Main runner script demonstrating all tasks
├── task8_fixed.py     # Debugged and fixed script
├── bonus_journal.py   # Student Journal v2 mini-project
├── report_en.docx     # Complete laboratory report
└── README.md          # Project documentation


🚀 Tasks Summary

Task 1: Positional and keyword argument practice with print_student_card().

Task 2: Default values and calculation logic with add_vat().

Task 3: Optional arguments handling with build_username().

Task 4: Dictionary generation combined with interactive while loops.

Task 5: In-place list mutation vs shallow copies with scores[:].

Task 6: Arbitrary arguments using *args and **kwargs.

Task 7: Modular programming and different import techniques.

Task 8: Identifying and fixing 4 syntax and logical errors.

Bonus: CLI student management journal with reporting and averages.

💻 How to Run

python lab8_main.py
python task8_fixed.py
python bonus_journal.py


👤 Author

Student: Ismet Gurbanov

Course: Fundamentals of Programming 1


---

## 5. Müdafiə Sualları və Qısa Cavablar (Xatırlatma)
1. **`return` əvəzinə `print` yazsaq nə olar?** `add_vat(100) + 10` `NoneType` və `int` toplanması xətası verər, çünki `print` dəyər qaytarmır (`None` qaytarır).
2. **Parametr və arqument fərqi:** Parametr funksiya təyin ediləndə mötərizə içindəki addır (`def f(x):`), arqument isə çağırış zamanı verilən faktiki dəyərdir (`f(5)`).
3. **`scores[:]` nədir?** Siyahının surətini (shallow copy) yaradır, funksiya bu kopyanı dəyişəndə əsas siyahı toxunulmaz qalır.
4. **`*numbers` hansı tipdədir?** `tuple` tipindədir (`print(type(numbers))` ilə yoxlanılır).
5. **`def f(a, b=1, c)` niyə xəta verir?** Default parametri olmayanlar (`c`) həmişə default parametri olanlardan (`b=1`) əvvəl yazılmalıdır.
