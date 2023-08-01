import PySimpleGUI as sg

label_1 = sg.Text("Enter feet:")
input_1 = sg.Input()

label_2 = sg.Text("Enter inches:")
input_2 = sg.Input()

compress_button = sg.Button("Convert")

window = sg.Window("Converter", layout=[[label_1, input_1], [label_2, input_2], [compress_button]])
window.read()
window.close()