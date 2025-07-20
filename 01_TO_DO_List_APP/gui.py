import functions
import time
import FreeSimpleGUI as fsg
import functions

label=fsg.Text("Type in a to-do")
input_box=fsg.InputText(tooltip="Enter a to-do",key='todo')
add_button=fsg.Button("Add")
list_box=fsg.Listbox(values=functions.get_todos(),key='todos',
size=[45,15],enable_events=True)
edit_button=fsg.Button("Edit")

window = fsg.Window("TO DO LIST APP", 
layout=[[label],[input_box,add_button],[list_box,edit_button]],
font=('Helvetica',15)
)
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit=values['todos'][0]
            new_todo=values['todo']+'\n'
            todos=functions.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case fsg.WIN_CLOSED:
            break
window.close()