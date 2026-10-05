budget = float(input("Enter your budget: "))
total = 0

while True:
    item = input("Enter item (or done): ")

    if item.lower() == "done":
        break

    price = float(input("Enter price: "))
    total += price

print("Total Shopping:", total)
print("Remaining:", budget - total)

if total <= budget:
    print("Within Budget")
else:
    print("Budget Exceeded")
