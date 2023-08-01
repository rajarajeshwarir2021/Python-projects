user_pwd = input("Enter new password: ")

result = []

if len(user_pwd) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in user_pwd:
    if i.isdigit():
        digit = True

result.append(digit)

uppercase = False
for i in user_pwd:
    if i.isupper():
        uppercase = True

result.append(uppercase)

if all(result):
    print("Strong Password")
else:
    print("Weak Password")


user_pwd = input("Enter new password: ")

result = {}

if len(user_pwd) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in user_pwd:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for i in user_pwd:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")