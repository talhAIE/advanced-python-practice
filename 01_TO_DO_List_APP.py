# To-Do List app
from operator import itemgetter


while True:
    user_action=input("Type add, show, edit, complete or exit: ")
    user_action=user_action.strip()

    match user_action:
        case 'add':
            todo=input("Enter a new item: ") + "\n"
            file=open('todo.txt','r')
            todos=file.readlines()
            todos.append(todo)
            file.close()

            file=open('todo.txt','w')
            file.writelines(todos)    
            file.close()

        case 'show' | 'display':

            with open('todo.txt','r') as file:
             todos=file.readlines()   
            for i,item in enumerate(todos):
                print(f"{i+1}. {item}")
            print(f"Total items: {len(todos)}")

        case 'edit':
            num=int(input("Enter the index number you want to edit: "))
            
            with open('todo.txt','r') as file:
                todos=file.readlines()
                todos[num-1]=input("Enter the new item: ") + "\n"
            with open('todo.txt','w') as file:
                file.writelines(todos)

        case 'complete':
            num=int(input("Enter the index number you want to complete: "))
            with open('todo.txt','r') as file:
                todos=file.readlines()
                complete=todos.pop(num-1)
                print(f"{complete} completed")
            with open('todo.txt','w') as file:
                file.writelines(todos)
        case 'exit' | 'quit':
            break
    
    # till day 6
    