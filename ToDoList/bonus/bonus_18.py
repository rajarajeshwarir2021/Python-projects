import PySimpleGUI as sg
from bonus.zip_extractor import extract_archive


label_1 = sg.Text("Select file to extract:")
input_1 = sg.Input()
choose_button_1 = sg.FilesBrowse("Choose", key='archivefile')

label_2 = sg.Text("Select destination folder:")
input_2 = sg.Input()
choose_button_2 = sg.FolderBrowse("Choose", key='destfolder')

extract_button = sg.Button("Extract")
output_label = sg.Text(key='output', text_color='yellow')

window = sg.Window("File Extractor",
                   layout=[[label_1, input_1, choose_button_1],
                           [label_2, input_2, choose_button_2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archive_filepath = values['archivefile']
    destination_folder = values['destfolder']
    extract_archive(archive_filepath, destination_folder)
    window['output'].update('Extraction completed!')

window.close()