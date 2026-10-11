temperatures = []

for i in range(7):
    temp = float(input(f"Day {i + 1} temperature: "))
    temperatures.append(temp)

highest = max(temperatures)
lowest = min(temperatures)
average = sum(temperatures) / len(temperatures)

print("\n--- Temperature Report ---")
print("Highest:", highest, "°C")
print("Lowest :", lowest, "°C")
print("Average:", round(average, 2), "°C")

if highest > 40:
    print("Warning: Extremely high temperature!")
