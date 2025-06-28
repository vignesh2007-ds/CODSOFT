import json
import os
import shutil
from datetime import datetime

FILENAME = "tasks.json"
BACKUP_FILE = "tasks_backup.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file, indent=4)
    backup()

def backup():
    shutil.copyfile(FILENAME, BACKUP_FILE)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(tasks):
        status = "✔️" if task['completed'] else "❌"
        due_date = task.get('due_date', '')
        priority = task.get('priority', 'Medium')
        category = task.get('category', 'General')
        overdue = ""
        if due_date:
            today = datetime.today().date()
            try:
                due = datetime.strptime(due_date, "%Y-%m-%d").date()
                if due < today and not task['completed']:
                    overdue = "⚠️ OVERDUE"
            except ValueError:
                overdue = "❗ Invalid date"
        print(f"{i+1}. [{status}] {task['title']} | {category} | Priority: {priority} | Due: {due_date} {overdue}")

    # Show progress
    completed = sum(t['completed'] for t in tasks)
    print(f"\n📊 Progress: {completed}/{len(tasks)} tasks completed ({(completed / len(tasks)) * 100:.1f}%)")

def add_task(tasks):
    title = input("\nEnter task name: ")
    category = input("Enter category (e.g., Work/School/Home): ") or "General"
    priority = input("Enter priority (High/Medium/Low): ") or "Medium"
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")

    tasks.append({
        "title": title,
        "completed": False,
        "category": category,
        "priority": priority,
        "due_date": due_date
    })
    save_tasks(tasks)
    print("✅ Task added!")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("\nEnter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            save_tasks(tasks)
            print("✅ Task marked complete.")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed['title']}' deleted.")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def export_tasks(tasks):
    import csv
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Completed", "Due Date", "Category", "Priority"])
        for task in tasks:
            writer.writerow([
                task['title'],
                task['completed'],
                task.get('due_date', ''),
                task.get('category', ''),
                task.get('priority', '')
            ])
    print("📤 Tasks exported to tasks.csv.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Export Tasks to CSV")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            export_tasks(tasks)
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid option. Try again.")

if __name__ == "__main__":
    main()
