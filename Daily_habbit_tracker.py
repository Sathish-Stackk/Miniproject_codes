habits = ["Exercise", "Study", "Reading", "Coding"]
completed = []

for habit in habits:
    answer = input(f"Did you complete {habit}? (yes/no): ")
    if answer.lower() == "yes":
        completed.append(habit)

print("\nCompleted Habits:")
for habit in completed:
    print("✓", habit)

print("Progress:", len(completed), "/", len(habits))
