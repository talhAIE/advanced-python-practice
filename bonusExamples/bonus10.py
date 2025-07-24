import FreeSimpleGUI as fsg
import zipextractor_bonus10

fsg.theme('Black')

text1=fsg.Text("Select Archive: ")
input1=fsg.Input(tooltip="Archive file to extract")
button1=fsg.FileBrowse("choose",key="archive")

text2=fsg.Text("Select Folder: ")
input2=fsg.Input(tooltip="Folder to save Extract Files")
button2=fsg.FolderBrowse("choose",key="extract")

button_main=fsg.Button("Extract")
output_label=fsg.Text(key="output",text_color="green")

layout=[
    [text1,input1,button1]
,[text2,input2,button2],
[button_main,output_label]
]

window=fsg.Window("Archive Extractor",
layout=layout,
font=('Helvetica',15)
)

while True:
    event,values=window.read()
    zipextractor_bonus10.extract_archive(values["archive"],values["extract"])
    window["output"].update("Extraction Completed!")
    break


window.close()