temp = float(input("Enter temperature (°C): "))

if temp < 10:
    advice = "Very cold - wear warm clothes"
elif temp < 20:
    advice = "Cool weather - carry a jacket"
elif temp < 30:
    advice = "Pleasant weather"
elif temp < 40:
    advice = "Hot weather - stay hydrated"
else:
    advice = "Extreme heat - avoid outdoor activity"

print("Advice:", advice)
