# A To-Do List application is a useful project that helps users manage and organize their tasks efficiently.
# This project aims to create a command-line or GUI-based application using Python, allowing users to create, 
# update, and track their to-do lists

from datetime import datetime

# Function to display the current tasks
def track_tasks(tasks):
    if not tasks:
        print("No tasks found. Add some tasks!")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['date']}")

# Function to add a new task
def create_task(tasks, title):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task = {'title': title, 'date': date}
    tasks.append(new_task)
    print(f"Task '{title}' created successfully!")

# Function to remove a task
def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task['title']}' deleted successfully!")
    else:
        print("Invalid task index.")

# Main function
def main():
    tasks = []

    while True:
        print("\nOptions:")
        print("1. Track Tasks")
        print("2. Create Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            track_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ")
            create_task(tasks, title)
        elif choice == '3':
            track_tasks(tasks)
            index = int(input("Enter the index of the task to remove: "))
            delete_task(tasks, index)
        elif choice == '4':
            print("Your To-Do-List is Upto date!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
