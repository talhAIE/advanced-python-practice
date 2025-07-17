# to avoid repetative code lets make custom functions
def get_todos(filepath):
    ''' Read a text from txt file and return a list of todos'''
    with open(filepath,'r') as file_local:
        todos_local=file_local.readlines()
    return todos_local

def write_todos(filepath,todos_args):
    ''' Write a list of todos in a txt file'''
    with open(filepath,'w') as file_local:
        file_local.writelines(todos_args)

if __name__=='__main__':
    print(get_todos('todo.txt'))