FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    # Open the file if it exist
    with open(filepath, 'r') as fh:
        todos_local = fh.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    # Write todo list to file
    with open(filepath, 'w') as fh:
        fh.writelines(todos_arg)