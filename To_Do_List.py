import json
from datetime import datetime

def load_todo_list():
    try:
        with open("todo_list.json", "r") as file:
            todo_list = json.load(file)
    except FileNotFoundError:
        todo_list = []
    return todo_list

def save_todo_list(todo_list):
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file, indent=2)

def display_todo_list(todo_list):
    print("\nTo-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task['title']} - {task['timestamp']}")

def add_task(todo_list, title):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task = {"title": title, "timestamp": timestamp}
    todo_list.append(new_task)
    save_todo_list(todo_list)
    print(f"\nTask '{title}' added successfully.")

def update_task(todo_list, index, new_title):
    if 1 <= index <= len(todo_list):
        todo_list[index - 1]["title"] = new_title
        todo_list[index - 1]["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_todo_list(todo_list)
        print(f"\nTask {index} updated successfully.")
    else:
        print("\nInvalid task index.")

def remove_task(todo_list, index):
    if 1 <= index <= len(todo_list):
        removed_task = todo_list.pop(index - 1)
        save_todo_list(todo_list)
        print(f"\nTask '{removed_task['title']}' removed successfully.")
    else:
        print("\nInvalid task index.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\nTo-Do List Application")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            title = input("Enter the task title: ")
            add_task(todo_list, title)
        elif choice == '3':
            display_todo_list(todo_list)
            try:
                index = int(input("Enter the index of the task to update: "))
                new_title = input("Enter the new task title: ")
                update_task(todo_list, index, new_title)
            except ValueError:
                print("\nInvalid input. Please enter a valid index.")
        elif choice == '4':
            display_todo_list(todo_list)
            try:
                index = int(input("Enter the index of the task to remove: "))
                remove_task(todo_list, index)
            except ValueError:
                print("\nInvalid input. Please enter a valid index.")
        elif choice == '5':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
