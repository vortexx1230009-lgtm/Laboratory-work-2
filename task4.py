def make_student(name, score, group=""):
    student = {"name": name, "score": score}
    if group:
        student["group"] = group
    return student
print(make_student("Kamran", 61, "CE-101"))
students = []
while True:
    name = input("Enter Your Name: (quit for exit the code) ")
    if name.lower() == "quit":
        break
    score = int(input("Enter Your Score: "))
    student = make_student(name, score)
    students.append(student)
for s in students:
    print(f"{s['name']}: {s['score']}")
