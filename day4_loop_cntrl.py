def display_menu():
    print("\n=====AI Engineer Study Planner====")
    print("1.Add a new task")
    print("View all tasks")
    print("3.Save nd Exit")
def show_tasks(tasks_list):
    print("\n ====Current Study Tasks====")
    if not tasks_list:
        print("Not tasks added yet")
    else:
        for index, tasks in enumerate(tasks_list, 1):
            print(f"{index}. {tasks}")
tasks=[]
keep_running=True
user_name=input("Enter u'r name: ")
while keep_running:
    display_menu()
    choice=input("Enter u'r choice(1-3): ")
    if choice=="1":
        new_task=input("Enter the new task:")
        tasks.append(new_task)
        print(f"Successfully added: {new_task}")
    elif choice=="2":
        show_tasks(tasks)
    elif choice=="3":
        print(f"\n Keep up the work, {user_name}...")
        keep_running=False
    else:
        print("Invalid choice! Kindly enter (1-3)")