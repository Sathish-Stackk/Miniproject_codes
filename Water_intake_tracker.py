glasses = int(input("Enter glasses of water today: "))

if glasses >= 8:
    print("Goal achieved! 💧")
else:
    remaining = 8 - glasses
    print("Drink", remaining, "more glass(es).")
