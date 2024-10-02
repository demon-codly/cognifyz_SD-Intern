import os

# Step 1: Define a Task class
class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"{self.task_id},{self.title},{self.description}"

    @staticmethod
    def from_string(task_string):
        task_id, title, description = task_string.split(',')
        return Task(int(task_id), title, description)

# List to store tasks
tasks = []

# File to store task data
TASK_FILE = "tasks.txt"

# Step 1: Read tasks from the file at the start
def load_tasks_from_file():
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, 'r') as file:
                for line in file:
                    task = Task.from_string(line.strip())
                    tasks.append(task)
        except Exception as e:
            print(f"Error reading file: {e}")

# Step 1: Save tasks to the file
def save_tasks_to_file():
    try:
        with open(TASK_FILE, 'w') as file:
            for task in tasks:
                file.write(str(task) + '\n')
    except Exception as e:
        print(f"Error writing to file: {e}")

# Step 2: Implement Create functionality
def create_task():
    task_id = len(tasks) + 1
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    new_task = Task(task_id, title, description)
    tasks.append(new_task)
    save_tasks_to_file()
    print("Task created and saved successfully!")

# Step 2: Implement Read functionality
def read_tasks():
    if tasks:
        print("\nCurrent Task List:")
        for task in tasks:
            print(f"ID: {task.task_id}, Title: {task.title}, Description: {task.description}")
    else:
        print("No tasks available.")

# Step 2: Implement Update functionality
def update_task():
    task_id = int(input("Enter the task ID to update: "))
    for task in tasks:
        if task.task_id == task_id:
            task.title = input("Enter new task title: ")
            task.description = input("Enter new task description: ")
            save_tasks_to_file()
            print("Task updated and saved successfully!")
            return
    print(f"Task with ID {task_id} not found.")

# Step 2: Implement Delete functionality
def delete_task():
    task_id = int(input("Enter the task ID to delete: "))
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            save_tasks_to_file()
            print("Task deleted and changes saved successfully!")
            return
    print(f"Task with ID {task_id} not found.")

# Main menu for user interaction
def main_menu():
    load_tasks_from_file()  # Load tasks when the program starts
    
    while True:
        print("\nTask Management Application")
        print("1. Create a new task")
        print("2. View tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_task()
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please try again.")

# Step 3: Test the application
if __name__ == "__main__":
    main_menu()
