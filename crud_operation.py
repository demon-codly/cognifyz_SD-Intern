# Step 1: Define a Task class
class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"ID: {self.task_id}, Title: {self.title}, Description: {self.description}"

# List to store tasks
tasks = []

# Step 2: Implement Create functionality
def create_task():
    task_id = len(tasks) + 1
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    new_task = Task(task_id, title, description)
    tasks.append(new_task)
    print("Task created successfully!")

# Step 3: Implement Read functionality
def read_tasks():
    if tasks:
        print("\nCurrent Task List:")
        for task in tasks:
            print(task)
    else:
        print("No tasks available.")

# Step 4: Implement Update functionality
def update_task():
    task_id = int(input("Enter the task ID to update: "))
    for task in tasks:
        if task.task_id == task_id:
            task.title = input("Enter new task title: ")
            task.description = input("Enter new task description: ")
            print("Task updated successfully!")
            return
    print(f"Task with ID {task_id} not found.")

# Step 5: Implement Delete functionality
def delete_task():
    task_id = int(input("Enter the task ID to delete: "))
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return
    print(f"Task with ID {task_id} not found.")

# Main menu for user interaction
def main_menu():
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

# Step 6: Test the application
if __name__ == "__main__":
    main_menu()
1