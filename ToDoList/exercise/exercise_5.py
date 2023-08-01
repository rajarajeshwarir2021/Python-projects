filenames = ['document', 'report', 'presentation']
for index, item in enumerate(filenames):
    print(f"{index}-{item.capitalize()}.txt")

ips = ['100.122.133.105', '100.122.133.111']
index = int(input("Enter the index of the IP you want: "))
print(f"You chose {ips[index]}")