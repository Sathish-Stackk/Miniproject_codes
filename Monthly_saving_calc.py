income = float(input("Enter monthly income: ₹"))
expenses = {
    "Food": 3000,
    "Travel": 1500,
    "Education": 2000,
    "Entertainment": 1000
}

total_expenses = sum(expenses.values())
savings = income - total_expenses

print("\n--- Monthly Financial Report ---")
for category, amount in expenses.items():
    print(f"{category}: ₹{amount}")

print("Total Expenses: ₹", total_expenses)
print("Remaining Savings: ₹", round(savings, 2))

if savings < 0:
    print("Warning: Expenses exceed income!")
else:
    print("Savings Rate:", round(savings / income * 100, 2), "%" if income else "")
