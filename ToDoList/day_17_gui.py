import PySimpleGUI as sg
from user_modules.user_def_functions import get_todos, write_todos

# Get todos list
todos = get_todos()

# Text labels
todo_label = sg.Text("Type in a to-do: ")

# Text input box
input_box = sg.InputText(tooltip="Enter todo", key="todo")

# Buttons
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

# Text output box
output_box = sg.Listbox(values=todos, key='todos', enable_events=True, size=[45, 10])

# Application window
app_window = sg.Window("My To-Do App",
                       layout=[[todo_label], [input_box, add_button], [output_box, edit_button]],
                       font=('Helvetica', 12))

while True:
    event, values = app_window.read()
    print(event)
    print(values)

    # Check for match conditions and perform the operation
    if event == 'Add':
        # Add new todo
        todo = values['todo'] + "\n"
        todos.append(todo)

    elif event == 'todos':
        app_window['todo'].update(value=values['todos'][0])

    elif event == 'Edit':
        # Edit a todo
        todo_to_edit = values['todos']
        index = todos.index(todo_to_edit)
        new_todo = values['todo'] + "\n"
        todos[index] = new_todo

    elif event == 'Complete':
        # Complete a todo
        pass

    elif sg.WIN_CLOSED:
        break

    app_window['todos'].update(values=todos)

write_todos(todos)

app_window.close()



