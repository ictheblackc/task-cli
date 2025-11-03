import sys
import os
import json
from datetime import datetime

FILE_NAME = 'tasks.json'


def add_task(task):
    pass


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
            pass
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