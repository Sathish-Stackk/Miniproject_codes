subjects = {}

while True:
    subject = input("Enter subject (or done): ")

    if subject.lower() == "done":
        break

    hours = float(input("Study hours: "))
    subjects[subject] = subjects.get(subject, 0) + hours

print("\nStudy Report")
for subject, hours in subjects.items():
    print(subject, ":", hours, "hours")

print("Total Hours:", sum(subjects.values()))
