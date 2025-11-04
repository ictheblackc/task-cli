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


def get_task(task):
    pass


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


def delete_task(task):
    pass


def change_status(id):
    pass


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
            pass
        case 'mark-in-progress':
            pass
        case 'mark-done':
            pass
        case 'list':
            pass
        case _:
            print(f"Unknown command: {cmd}")


if __name__ == '__main__' :
    main()