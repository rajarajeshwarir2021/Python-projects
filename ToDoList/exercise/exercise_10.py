try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    if total_value == 0.0:
        exit("Your total value cannot be zero.")

    percentage = (value / total_value) * 100
    print(f"That is {percentage}%")


except ValueError:
    print("You need to enter a number. Run the program again.")



