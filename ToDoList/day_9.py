filename = "files/todos.txt"

# Open the file if it exist
with open(filename, 'r') as fh:
    todos = fh.readlines()

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # Check for match conditions and perform the operation
    if 'add' in user_action:
        # Add new todo
        todo = user_action[4:] + "\n"
        todos.append(todo)

    elif 'show' in user_action:
        # Show the todos list items
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1} - {item}")

    elif 'edit' in user_action:
        # Edit a todo
        number = int(user_action[5:])
        number = number - 1
        new_todo = input("Enter new todo: ") + "\n"
        todos[number] = new_todo

    elif 'complete' in user_action:
        # Complete a todo
        number = int(user_action[9:])
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        message = f"Todo '{todo_to_remove}' was removed from the list."
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print("Command is not valid.")

# Write todo list to file
with open(filename, 'w') as fh:
    fh.writelines(todos)

print("Bye!")
