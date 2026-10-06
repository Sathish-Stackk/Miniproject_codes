import time

minutes = int(input("Enter study time in minutes: "))
seconds = minutes * 60

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60
    print(f"Time Left: {mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)
    seconds -= 1

print("\nStudy session completed!")
