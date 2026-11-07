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
    choice = input("Choice: (1 - Add student, 2 - Report, 3 - Quit) ")
    if choice == "1":
        name = input("Name: ")
        score = int(input("Score: "))
        add_student(students, name, score)
    elif choice == "2":
        print_report(students)
    elif choice == "3":
        break
    else:
        print("Yanlış seçim, yeniden cehd edin")
