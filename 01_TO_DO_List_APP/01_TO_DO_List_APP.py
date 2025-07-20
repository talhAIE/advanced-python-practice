# TO do list
from functions import get_todos,write_todos
import time
time_now=time.strftime("%b %d, %Y %H:%M:%S")
print(f"it is {time_now}")
while True:
    user_action=input("Type add, show, edit, complete or exit: ")
    user_action=user_action.strip()

    if  user_action.startswith('add'):
        todo=user_action[4:]
        todos=get_todos('todo.txt')
        todos.append(todo+'\n')
        write_todos("todo.txt",todos)

    elif user_action.startswith('show'):
        todos=get_todos('todo.txt')     
        for i,item in enumerate(todos):
            print(f"{i+1}. {item.strip('\n')}")
        print(f"Total items: {len(todos)}")

    elif user_action.startswith('edit'):
        try:
            num=int(user_action[5:])
            todos=get_todos(filepath='todo.txt')
            todos[num-1]=input("Enter the new item: ") + "\n"
            write_todos("todo.txt",todos)
        except ValueError:
            print("Your Enter wrong input")
            continue

    elif user_action.startswith('complete'):
        try:
            num=int(user_action[9:])
            todos=get_todos('todo.txt')
            complete=todos.pop(num-1)
            print(f"{complete} completed")
            write_todos("todo.txt",todos)
        except IndexError:
            print("There is no item with that number")
    elif 'exit' in user_action or 'quit' in user_action:
        break
    else:
        print("Invalssid input")

    # till day 1