LOWER_TEMPERATURE = 0
HIGHER_TEMPERATURE = 100

user_temperature = int(input("Enter water temperature: "))

if user_temperature < 0:
    print("Solid")
elif user_temperature < 100:
    print("Water")
elif user_temperature >= 100:
    print("Gas")
else:
    print("Invalid input value")
