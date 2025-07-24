from logging import PlaceHolder
import streamlit as st
import functions

todos=functions.get_todos()
st.set_page_config(layout="wide")
   
def add_todo():
    todo=st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
st.title("Todo List APP")
st.subheader("This is a simple todo list app")
st.write("This app is to increase your <b>productivity</b>",unsafe_allow_html=True)

for i,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="",placeholder="Add a new todo...",
on_change=add_todo,key='new_todo')


