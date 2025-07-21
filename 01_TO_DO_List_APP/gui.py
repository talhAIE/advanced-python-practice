import functions
import time
import FreeSimpleGUI as fsg
import functions
fsg.theme("GreenTan")
label=fsg.Text("Type in a to-do")

input_box=fsg.InputText(tooltip="Enter a to-do",key='todo')

add_button=fsg.Button(size=7,image_source="01_TO_DO_List_APP/add.png",key='Add' )

clock_text=fsg.Text(" ",key='clock')
list_box=fsg.Listbox(values=functions.get_todos(),key='todos',
size=[45,15],enable_events=True)
edit_button=fsg.Button("Edit")

complete_button=fsg.Button("complete")
exit_button=fsg.Button("Exit")

layout=[
    [clock_text],
    [label],
[input_box,add_button],
[list_box,edit_button,complete_button],
[exit_button]
]

window = fsg.Window("TO DO LIST APP", 
layout=layout,
font=('Helvetica',15)
)
while True:
    event,values=window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit=values['todos'][0]
                new_todo=values['todo']+'\n'
                todos=functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item first",font=("Helvetica",15))
        
        case 'todos':
            window['todo'].update(value=values['todos'][0])  

        case 'Complete':
            try:
                todos=functions.get_todos()
                todo_complete=values['todos'][0]
                todos.remove(todo_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except:
                fsg.popup("Please select an item first",font=("Helvetica",15))

        case "Exit":
            break
        case fsg.WIN_CLOSED:
            break
window.close()