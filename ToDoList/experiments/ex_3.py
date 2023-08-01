todos = []

while True:
    user_action = input("Type add, show, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item.title())
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")

