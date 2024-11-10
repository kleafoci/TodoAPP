import streamlit as st
from streamlit import checkbox

import functionscopy

todos = functionscopy.get_todos()

def add_todo():
    todo= st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functionscopy.write_todos(todos)

st.title("My Todo App")
st.write("Click on the box to remove completed todos.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functionscopy.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
