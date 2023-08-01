import time
import PySimpleGUI as sg
from user_modules.user_def_functions import get_todos, write_todos

# Theme of the GUI
sg.theme('Black')
# Get todos list
todos = get_todos()

# Text labels
clock = sg.Text('', key='clock')
todo_label = sg.Text("Type in a to-do: ")

# Text input box
input_box = sg.InputText(tooltip="Enter todo", key="todo")

# Buttons
add_button = sg.Button("Add", size=10, mouseover_colors="LightBlue2", tooltip="Add todo")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# Text output box
output_box = sg.Listbox(values=todos, key='todos', enable_events=True, size=[45, 10])

# Application window
app_window = sg.Window("My To-Do App",
                       layout=[[clock], [todo_label], [input_box, add_button], [output_box, edit_button, complete_button], [exit_button]],
                       font=('Helvetica', 12))

while True:
    event, values = app_window.read(timeout=10)
    app_window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
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
        try:
            todo_to_edit = values['todos']
            index = todos.index(todo_to_edit)
            new_todo = values['todo'] + "\n"
            todos[index] = new_todo
        except ValueError:
            sg.popup("Please select an item first.", font=('Helvetica', 12))
            continue

    elif event == 'Complete':
        # Complete a todo
        try:
            todo_to_complete = values['todos'][0]
            todos.remove(todo_to_complete)
            app_window['todos'].update(value=todos)
            app_window['todo'].update(value='')
        except ValueError:
            sg.popup("Please select an item first.", font=('Helvetica', 12))
            continue

    elif event == 'Exit':
        break

    elif sg.WIN_CLOSED:
        break

    app_window['todos'].update(values=todos)

write_todos(todos)

app_window.close()



