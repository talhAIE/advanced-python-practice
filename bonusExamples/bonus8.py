# import FreeSimpleGUI as fsg

# label1=fsg.Text("Select files to compress")
# input1=fsg.Input()
# choose_button=fsg.FilesBrowse("Choose")
# label2=fsg.Text("Select destination Folders")
# input2=fsg.Input()
# choose_button2=fsg.FolderBrowse("Choose")
# compress_button=fsg.Button("Compress")
# window=fsg.Window("File Compressor",
# layout=[[label1,input1,choose_button],[label2,input2,choose_button2],[compress_button]]
# )
# window.read()
# window.close()

# coding exercise
import FreeSimpleGUI as fsg
label1=fsg.Text("Enter feet:")
input1=fsg.Input()
label2=fsg.Text("Enter inches:")
input2=fsg.Input()
convert_button=fsg.Button("Convert")
window=fsg.Window("Converter",layout=[[label1,input1],[label2,input2],[convert_button]])
window.read()
window.close()