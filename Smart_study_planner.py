subjects = {
    "Python": 2,
    "DSA": 3,
    "React": 1,
    "Database": 2
}

total_hours = sum(subjects.values())

for subject, hours in sorted(
    subjects.items(), key=lambda item: item[1], reverse=True
):
    print(f"{subject}: {hours} hours")

print("Total Study Hours:", total_hours)
print("Daily Average:", round(total_hours / len(subjects), 1), "hours")
