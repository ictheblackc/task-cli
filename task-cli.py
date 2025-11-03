import sys
import os
import json
from datetime import datetime

FILE_NAME = 'tasks.json'


def add_task(description):
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
    print(f"New task with ID {id} was successfully added")


def get_task(task):
    pass


def update_task(task):
    pass


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
            pass
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