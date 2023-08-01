user_country = input("Enter your country: ")

match user_country:
    case 'USA':
        print("Hello")
    case 'India':
        print("Namaste")
    case 'Germany':
        print("Hallo")

ingredients = ["john smith", "sen plakay", "dora ngacely"]
for i in ingredients:
    print(i.title())