# todo.py

todo_list = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Mark task as done")
    print("4. Exit")

def show_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        for i, task in enumerate(todo_list):
            status = "✓" if task['done'] else "✗"
            print(f"{i + 1}. {task['task']} [{status}]")

def add_task():
    task_name = input("Enter your task: ")
    todo_list.append({'task': task_name, 'done': False})
    print("Task added!")

def mark_done():
    show_tasks()
    task_number = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= task_number < len(todo_list):
        todo_list[task_number]['done'] = True
        print("Task marked as done!")
    else:
        print("Invalid number!")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Goodbye 👋")
        break
    else:
        print("Please choose a valid option.")
