filename = "files/todos.txt"

# Open the file if it exist
with open(filename, 'r') as fh:
    todos = fh.readlines()

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # Check for match conditions and perform the operation
    if user_action.startswith('add'):
        # Add new todo
        todo = user_action[4:] + "\n"
        todos.append(todo)

    elif user_action.startswith('show'):
        # Show the todos list items
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1} - {item}")

    elif user_action.startswith('edit'):
        # Edit a todo
        try:
            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo
        except ValueError:
            print("Your command is Invalid")
            continue

    elif user_action.startswith('complete'):
        # Complete a todo
        try:
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("Index Number out of range")

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid.")

# Write todo list to file
with open(filename, 'w') as fh:
    fh.writelines(todos)

print("Bye!")
