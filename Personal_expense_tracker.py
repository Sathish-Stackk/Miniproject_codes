expenses = []

def add_expense(name, amount):
    expenses.append({"name": name, "amount": amount})

def show_expenses():
    for item in expenses:
        print(f"{item['name']}: ₹{item['amount']}")

    total = sum(item["amount"] for item in expenses)
    print("Total Expenses: ₹", total)

add_expense("Food", 150)
add_expense("Travel", 80)
add_expense("Books", 300)
show_expenses()
