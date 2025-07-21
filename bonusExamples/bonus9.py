from turtle import color
import FreeSimpleGUI as fsg
import zipcreater_bonus9

label1=fsg.Text("Select files to compress")
input1=fsg.Input()
choose_button=fsg.FilesBrowse("Choose",key='files')

label2=fsg.Text("Select destination Folders")
input2=fsg.Input()
choose_button2=fsg.FolderBrowse("Choose",key='folder')

compress_button=fsg.Button("Compress")
out_put_text=fsg.Text(key='output',text_color='green')
window=fsg.Window("File Compressors",
layout=[[label1,input1,choose_button],[label2,input2,choose_button2],[compress_button,out_put_text]]
)

while True:
    event,values=window.read()
    file_paths=values['files']
    folder_path=values['folder']
    print(file_paths)
    print(folder_path)
    
    if event==fsg.WIN_CLOSED:
        break
    elif event=='Compress':
        
        zipcreater_bonus9.create_zip(file_paths.split(';'),folder_path)
        window['output'].update(value='Compression Completed')

    

window.close()