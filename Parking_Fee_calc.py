hours = int(input("Enter parking hours: "))

if hours <= 1:
    fee = 20
elif hours <= 3:
    fee = 20 + (hours - 1) * 15
else:
    fee = 50 + (hours - 3) * 10

print("Parking Fee: ₹", fee)
