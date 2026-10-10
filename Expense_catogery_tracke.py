expenses = {
    "Food": [120, 80, 150],
    "Travel": [60, 100],
    "Shopping": [300, 450],
    "Bills": [500]
}

for category, values in expenses.items():
    print(category, "=", sum(values))

total = sum(sum(values) for values in expenses.values())
print("Total Expense:", total)
