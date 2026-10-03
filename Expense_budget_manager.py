budget = 5000

expenses = {
    "Food": 1200,
    "Travel": 800,
    "Shopping": 1500,
    "Education": 600
}

total = sum(expenses.values())
remaining = budget - total

print("----- Expense Report -----")

for category, amount in expenses.items():
    print(f"{category}: ₹{amount}")

print("--------------------------")
print("Budget: ₹", budget)
print("Total Spent: ₹", total)
print("Remaining: ₹", remaining)

if remaining >= 0:
    print("Status: Within Budget")
else:
    print("Status: Budget Exceeded")
