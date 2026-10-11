inventory = {
    "Laptop": 5,
    "Mouse": 12,
    "Keyboard": 8,
    "Headphones": 6
}

item = input("Enter product name: ")

if item in inventory:
    print("Current Stock:", inventory[item])

    sold = int(input("Enter quantity sold: "))

    if sold <= inventory[item]:
        inventory[item] -= sold
        print("Updated Stock:", inventory[item])
    else:
        print("Not enough stock.")
else:
    print("Product not found.")
