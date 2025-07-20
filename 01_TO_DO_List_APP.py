todo=[]

while True:
    user_action=input("Type add, show, edit, exit: ")
    user_action=user_action.strip().lower()

    match user_action:
        case 'add':
            todo_item=input("Enter a todo item: ")
            todo.append(todo_item)
        
        case 'show' | 'display':
            for item in todo:
                print(item)
        
        case 'edit':
            number=int(input("Enter the number of the todo item to edit: "))
            number-=1
            todo[number]=input("Enter the new todo item: ")      
        case 'exit' | 'quit':
            break

        case _:
            print("Invalid command. please try again.")
print('Goodbye!')