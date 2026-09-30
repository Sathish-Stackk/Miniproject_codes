students = {
    "Sathish": [85, 90, 78],
    "Rahul": [72, 68, 80],
    "Priya": [95, 92, 88]
}

for name, marks in students.items():
    average = sum(marks) / len(marks)
    grade = "A" if average >= 85 else "B" if average >= 70 else "C"

    print(f"{name}: Average={average:.1f}, Grade={grade}")
