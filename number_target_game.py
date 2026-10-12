import random

target = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Guess the number (1-50): "))
    attempts += 1

    if guess == target:
        print(f"Correct! Attempts: {attempts}")
        break
    elif guess < target:
        print("Try a higher number")
    else:
        print("Try a lower number")
