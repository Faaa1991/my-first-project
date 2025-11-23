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
while True:
    show_menu()
    choice = input("Choose: ")
    
    if choice == "1":
        add_todo(input("Enter TODO: "))
    elif choice == "2":
        list_todos()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
def save_todos():
    with open("todos.txt", "w") as f:
        for t in todos:
            f.write(t + "\n")
def load_todos():
    try:
        with open("todos.txt", "r") as f:
            for line in f:
                todos.append(line.strip())
    except FileNotFoundError:
        pass

load_todos()
def delete_todo(index):
    if 0 <= index < len(todos):
        todos.pop(index)
def list_todos():
    if not todos:
        print("No todos yet!")
        return
    for i, t in enumerate(todos, start=1):
        print(f"[{i}] {t}")
print("3. Delete TODO")
print("4. Exit")
def edit_todo(index, new_text):
    if 0 <= index < len(todos):
        todos[index] = new_text
