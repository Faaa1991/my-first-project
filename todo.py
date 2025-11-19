print("Simple TODO App")
todos = []

def show_menu():
    print("1. Add TODO")
    print("2. List TODOs")
    print("3. Exit")

def add_todo(item):
    todos.append(item)

def list_todos():
    for i, t in enumerate(todos):
        print(f"{i+1}. {t}")
