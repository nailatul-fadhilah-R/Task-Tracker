import sys
import json
import os
from datetime import datetime

JSON_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(JSON_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# --- Features ---

def add_task(description):
    tasks = load_tasks()
    new_id = max([t['id'] for t in tasks], default=0) + 1
    now = datetime.now().isoformat()
    
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == int(task_id):
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Error: Task {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t["id"] != int(task_id)]
    if len(tasks) == len(updated_tasks):
        print(f"Error: Task {task_id} not found.")
    else:
        save_tasks(updated_tasks)
        print(f"Task {task_id} deleted successfully.")

def mark_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == int(task_id):
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"Error: Task {task_id} not found.")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        if filter_status and task["status"] != filter_status:
            continue
        print(f"[{task['id']}] {task['description']} - {task['status']} (Updated: {task['updatedAt']})")


def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py [command] [arguments]")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        add_task(sys.argv[2])
    elif command == "update" and len(sys.argv) > 3:
        update_task(sys.argv[2], sys.argv[3])
    elif command == "delete" and len(sys.argv) > 2:
        delete_task(sys.argv[2])
    elif command == "mark-in-progress" and len(sys.argv) > 2:
        mark_status(sys.argv[2], "in-progress")
    elif command == "mark-done" and len(sys.argv) > 2:
        mark_status(sys.argv[2], "done")
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    else:
        print("Invalid command or missing arguments.")

if __name__ == "__main__":
    main()