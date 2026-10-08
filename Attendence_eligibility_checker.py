total_classes = int(input("Enter total classes: "))
attended = int(input("Enter classes attended: "))

percentage = (attended / total_classes) * 100

print("Attendance:", round(percentage, 2), "%")

if percentage >= 75:
    print("Eligible for examination")
else:
    print("Not eligible for examination")
