import sys
import os
import json
from datetime import datetime

# File where all tasks are stored
FILE_NAME = 'tasks.json'


def add_task(description):
    """Add a new task to the list."""
    tasks = load_tasks()

    ids = [t['id'] for t in tasks]
    id = max(ids) + 1 if ids else 1

    now = datetime.now().isoformat()

    task = {
        'id': id,
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now,
    }
    tasks.append(task)

    save_tasks(tasks)
    print(f"Task #{id} has been added.")


def update_task(id, description):
    """Update description of an existing task."""
    tasks = load_tasks()

    for t in tasks:
        if t['id'] == int(id):
            t['description'] = description
            t['updatedAt'] = datetime.now().isoformat()

            save_tasks(tasks)
            print(f"Task #{id} has been updated.")
            return

    print(f"Task #{id} not found.")


def delete_task(id):
    """Delete a task by its ID."""
    tasks = load_tasks()

    for t in tasks:
        if t['id'] == int(id):
            tasks.remove(t)

            save_tasks(tasks)
            print(f"Task #{id} has been deleted.")
            return

    print(f"Task #{id} not found.")


def change_status(id, status):
    """Change the status of a task (todo, in-progress, done)."""
    tasks = load_tasks()

    for t in tasks:
        if t['id'] == int(id):
            t['status'] = status
            t['updatedAt'] = datetime.now().isoformat()

            save_tasks(tasks)
            print(f"Task status #{id} has been changed.")
            return

    print(f"Task #{id} not found.")


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f)


def show_tasks(status=None):
    """Display all tasks or only those with a specific status."""
    tasks = load_tasks()

    if status:
        tasks = [t for t in tasks if t['status'] == status]

    if not tasks:
        print("No tasks yet.")
        return

    for t in tasks:
        created = t['createdAt'][:10]
        updated = t['updatedAt'][:10]
        date = created if created == updated else updated
        print(f"#{t['id']} [{t['status']}] {t['description']} ({date})")


def main():
    """Command-line interface handler."""
    args = sys.argv[1:]

    if not args:
        print("Usage: task-cli <command> [arguments]")
        return

    cmd = args[0]

    match cmd:
        case 'add':
            if len(args) < 2:
                print("Usage: add [description]")
                return
            description = " ".join(args[1:])
            add_task(description)
        case 'update':
            if len(args) < 3:
                print("Usage: update [id] [description]")
                return
            id = args[1]
            description = " ".join(args[2:])
            update_task(id, description)
        case 'delete':
            if len(args) < 2:
                print("Usage: delete [id]")
                return
            id = args[1]
            delete_task(id)
        case 'mark-in-progress':
            if len(args) < 2:
                print("Usage: mark-in-progress [id]")
                return
            id = args[1]
            change_status(id, 'in-progress')
        case 'mark-done':
            if len(args) < 2:
                print("Usage: mark-done [id]")
                return
            id = args[1]
            change_status(id, 'done')
        case 'list':
            status = args[1] if len(args) > 1 else None
            show_tasks(status)
        case _:
            print(f"Unknown command: {cmd}")


if __name__ == '__main__':
    main()
