distance = float(input("Enter distance in km: "))
passengers = int(input("Enter number of passengers: "))

if distance <= 10:
    fare = 15
elif distance <= 25:
    fare = 25
else:
    fare = 40

total = fare * passengers

print("Fare per passenger: ₹", fare)
print("Total Fare: ₹", total)
