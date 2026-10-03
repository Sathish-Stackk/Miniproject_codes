students = {
    "Sathish": [85, 78, 92],
    "Rahul": [65, 72, 68],
    "Priya": [91, 88, 95]
}

print("----- Student Results -----")

for name, marks in students.items():
    average = sum(marks) / len(marks)

    if average >= 85:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    print(f"{name}: {average:.2f}% - Grade {grade}")
