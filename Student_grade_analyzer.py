def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


name = input("Enter student name: ")
marks = []

for i in range(3):
    marks.append(float(input(f"Enter subject {i + 1} marks: ")))

print("\n--- Student Report ---")
print("Name:", name)
print("Total:", sum(marks))
print("Average:", round(sum(marks) / 3, 2))
print("Grade:", calculate_grade(marks))
