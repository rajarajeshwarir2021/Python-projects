import PySimpleGUI as sg
import user_modules.user_def_functions


todo_label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

app_window = sg.Window("My To-Do App", layout=[[todo_label, input_box, add_button]])
app_window.read()
app_window.close()



