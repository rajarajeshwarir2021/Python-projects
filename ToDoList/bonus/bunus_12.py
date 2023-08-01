feet_inches = input("Enter feet and inches:")

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters

result = convert(feet_inches)

print(f"{feet_inches} feet is equal to {result} meters.")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")

