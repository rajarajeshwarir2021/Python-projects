filename = "files/todos.txt"

with open(filename, 'r') as fh:
    todos = fh.readlines()

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                print(f"{index + 1} - {item}")
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break

with open(filename, 'w') as fh:
    fh.writelines(todos)

print("Bye!")
