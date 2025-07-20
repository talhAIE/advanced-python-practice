import functions
import time
import FreeSimpleGUI as fsg


label=fsg.Text("Type in a to-do")
input_box=fsg.InputText(tooltip="Enter a to-do")
add_button=fsg.Button("Add")
window = fsg.Window("My Window", layout=[[label],[input_box,add_button]])
window.read()
window.close()