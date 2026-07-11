FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    try:
        with open(filepath, "r") as file:
            todos = file.readlines()
    except FileNotFoundError:
        todos = []

    return todos


def write_todos(todos, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos)