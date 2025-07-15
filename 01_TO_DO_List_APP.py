# TO do list
while True:
    user_action=input("Type add, show, edit, complete or exit: ")
    user_action=user_action.strip()

    if  user_action.startswith('add'):
        todo=user_action[4:]
        with open('todo.txt','r') as file:
            todos=file.readlines()
            todos.append(todo+'\n')
        with open('todo.txt','w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        with open('todo.txt','r') as file:
            todos=file.readlines()
            
        for i,item in enumerate(todos):
            print(f"{i+1}. {item.strip('\n')}")
        print(f"Total items: {len(todos)}")

    elif user_action.startswith('edit'):
        try:
            num=int(user_action[5:])
            with open('todo.txt','r') as file:
                todos=file.readlines()
                todos[num-1]=input("Enter the new item: ") + "\n"
            with open('todo.txt','w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your Enter wrong input")
            continue

    elif user_action.startswith('complete'):
        try:
            num=int(user_action[9:])
            with open('todo.txt','r') as file:
                todos=file.readlines()
                complete=todos.pop(num-1)
                print(f"{complete} completed")
            with open('todo.txt','w') as file:
                file.writelines(todos)
        except IndexError:
            print("There is no item with that number")
    elif 'exit' in user_action or 'quit' in user_action:
        break
    else:
        print("Invalid input")

    # till day 10