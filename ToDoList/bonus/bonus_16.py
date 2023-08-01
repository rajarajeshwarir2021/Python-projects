import PySimpleGUI as sg

label_1 = sg.Text("Select files to compress:")
input_1 = sg.Input()
choose_button_1 = sg.FilesBrowse("Choose")

label_2 = sg.Text("Select destination folder:")
input_2 = sg.Input()
choose_button_2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[label_1, input_1, choose_button_1], [label_2, input_2, choose_button_2], [compress_button]])
window.read()
window.close()