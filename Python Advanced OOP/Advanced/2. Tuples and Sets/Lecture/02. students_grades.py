students_grades = {}

for _ in range(int(input())):
    name, grade = input().split()

    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(float(grade))

for student, grades in students_grades.items():
    convert_grades_to_string = " ".join(map(lambda current_grade: f"{current_grade:.2f}", grades))
    average_grade = sum(grades) / len(grades)

    print(f"{student} -> {convert_grades_to_string} (avg: {average_grade:.2f})")