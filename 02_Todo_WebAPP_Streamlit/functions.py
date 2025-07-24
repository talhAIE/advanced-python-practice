# to avoid repetative code lets make custom functions

FILEPATH='02_Todo_WebAPP_Streamlit/todo.txt'
def get_todos(file_path=FILEPATH):
    ''' Read a text from txt file and return a list of todos'''
    with open(file_path,'r') as file_local:
        todos_local=file_local.readlines()
    return todos_local

def write_todos(todos_args,file_path=FILEPATH,):
    ''' Write a list of todos in a txt file'''
    with open(file_path,'w') as file_local:
        file_local.writelines(todos_args)

if __name__=='__main__':
    print(get_todos('todo.txt'))