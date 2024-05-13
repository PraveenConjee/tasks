def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                tasks.append(task.strip())
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print("Error saving tasks:", e)

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def remove_task(tasks):
    try:
        index = int(input("Enter the index of the task to remove: "))
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print("Error removing task:", e)

def view_tasks(tasks, file_name):
    try:
        with open(file_name, "w") as file:
            file.write("Tasks:\n")
            for task in tasks:
                file.write(task + "\n")
        print("Tasks written to '{}' successfully.".format(file_name))
    except Exception as e:
        print("Error writing tasks to file:", e)

def main():
    tasks = load_tasks()
    while True:
        print("\nTask List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            name = input("Enter file name: ")
            view_tasks(tasks, name)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


main()
