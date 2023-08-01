filename = "files/todos.txt"

# Open the file if it exist
with open(filename, 'r') as fh:
    todos = fh.readlines()

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # Check for match conditions and perform the operation
    match user_action:
        case 'add':
            # Add new todo
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
        case 'show':
            # Show the todos liat items
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1} - {item}")
        case 'edit':
            # Edit a todo
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo
        case 'complete':
            # Complete a todo
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break

# Write todo list to file
with open(filename, 'w') as fh:
    fh.writelines(todos)

print("Bye!")
