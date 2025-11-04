import sys
import os
import json
from datetime import datetime

FILE_NAME = 'tasks.json'


def add_task(description):
    tasks = load_tasks()
    
    ids = [t['id'] for t in tasks]
    id = max(ids) + 1 if ids else 1

    task = {
        'id': id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat(),
    }
    tasks.append(task)

    save_tasks(tasks)
    print(f"Task #{id} has been added.")


def update_task(id, description):
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
    tasks = load_tasks()

    for t in tasks:
        if t['id'] == int(id):
            tasks.remove(t)

            save_tasks(tasks)
            print(f"Task #{id} has been deleted.")
            return
    
    print(f"Task #{id} not found.")


def change_status(id, status):
    tasks = load_tasks()

    for t in tasks:
        if t['id'] == int(id):
            t['status'] = status

            save_tasks(tasks)
            print(f"Task status #{id} has been changed.")
            return
    
    print(f"Task #{id} not found.")


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f)


def show_tasks(status=None):
    tasks = load_tasks()

    if status:
        tasks = [t for t in tasks if t['status'] == status]

    if not tasks:
        print("No tasks yet.")
        return

    for t in tasks:
        print(f"#{t['id']} [{t['status']}] {t['description']}")


def main():
    args = sys.argv[1:]

    if not args:
        return
    
    cmd = args[0]
    
    match cmd:
        case 'add':
            description = " ".join(args[1:])
            add_task(description)
        case 'update':
            id = args[1]
            description = " ".join(args[2:])
            update_task(id, description)
        case 'delete':
            id = args[1]
            delete_task(id)
        case 'mark-in-progress':
            id = args[1]
            change_status(id, 'in-progress')
        case 'mark-done':
            id = args[1]
            change_status(id, 'done')
        case 'list':
            status = args[1] if len(args) > 1 else None
            show_tasks(status)
        case _:
            print(f"Unknown command: {cmd}")


if __name__ == '__main__' :
    main()