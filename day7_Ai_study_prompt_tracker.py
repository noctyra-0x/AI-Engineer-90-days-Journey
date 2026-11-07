study_logs=[]
def display_menu():
    """Displays Interactive Terminal Option"""
    print("\n============================")
    print("AI Study Prompt Tracker")
    print("==============================")
    print("1.Log a study session")
    print("2.View all study logs")
    print("3.View total study hours")
    print("Exit")
def log_session():
    topic=input("\n Enter topic studied: ").strip()
    while True:
        try:
            hours=float(input("Enter spent hours:   "))
            if hours <=0:
                print("Hours must be greater than 0")
                continue
            break
        except ValueError:
            print("Enter the valid number for hours")
    notes=input("Enter the key takeway  or prompt notes: ").strip()
    log_entry={
        "topic": topic,
        "hours": hours,
        "notes": notes
    }
    study_logs.append(log_entry)
    print(f"\n Success: Logged session for {topic}")
def view_logs():
    print("\n==============================")
    print("         All Study Logs          ")
    print("-------------------------------")
    if not study_logs():
        print("\n No study sessions logged yet")
        return
    for idx, log in enumerate(study_logs, 1):
        print(f"{idx}  Topic: {log['topic']}")
        print(f"Hours: {log['hours']} hrs")
        print(f"Notes: {log['notes']}\n")
def view_total_hours():
    if not study_logs():
        print("\n No hours logged yet")
        return
    total=sum(log["hours"] for log in study_logs)
    print("\n Total study time recorded: {total:.1f} hours")  
print("Welcome to Your AI ENGINEERING TRACK")
user_name=input("Enter your name: ")
while True:
    display_menu()
    choice=input("\n Choose an option (1-4)").strip()
    if choice =="1":
        log_session()
    elif choice =="2":
        view_logs()
    elif choice =="3":
        view_total_hours()
    
    elif choice =="4":
        print("\n Awesome progress this week, {user_name}!!")
    break
else:
    print("Invalid choice, Kindly enter (1-4)")