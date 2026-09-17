# to-do list
task = []

def add_task():
    limit = int(input("how many task you want to add: "))

    for i in range(limit):
        tasks = input("Enter task: ")
        task.append(tasks)
    print("Added successfully""\n")

def view_task():
    if len(task) == 0:
        print("There's no task in the list!""\n")
    else:
        for i,taskss in enumerate(task,1):
            print(i,taskss)
def delete_task():


    if len(task) > 0:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(task):
            deleted_task = task.pop(number - 1)
            print("Deleted:", deleted_task,"\n")
        else:
            print("Invalid task number.","\n")

while True:
    print("----To-Do List----""\n")

    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit""\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_task()

    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("List exited""\n")
    else:
        print("Invalid choice""\n")