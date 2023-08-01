import streamlit as st
from user_modules.user_def_functions import get_todos, write_todos


todos = get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for idx, todo in enumerate(todos):
    task_checkbox = st.checkbox(todo, key=todo)
    if task_checkbox:
        todos.pop(idx)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo... ", on_change=add_todo, key='new_todo')


