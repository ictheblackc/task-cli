
# task-cli

![Preview](preview.gif)

**task-cli** is a simple command-line application for managing your tasks. 

It allows you to **add, update, delete, and track tasks** with different statuses (`todo`, `in-progress`, `done`).

All tasks are stored in a local JSON file (`tasks.json`) in the current directory.

> **Note:** This project was created as a solution for the **Task Tracker** exercise from [roadmap.sh](https://roadmap.sh) to help beginners practice building a CLI app. Some details have been simplified. However, the code can still be used as an example.

## Installation

```
git clone git@github.com:ictheblackc/task-cli.git
```

## Usage

**The general syntax**
```bash
python task-cli.py <command> [arguments]
```

**Add a task**
```bash
python task-cli.py add <description>
```

**Update a task**
```bash
python task-cli.py update <id> <description>
```

**Delete a task**
```bash
python task-cli.py delete <id>
```

**Change task status**

Mark a task as `in progress`:
```bash
python task-cli.py mark-in-progress <id>
```
Mark a task as `done`:
```bash
python task-cli.py mark-done <id>
```

**List tasks**

List all tasks:
```bash
python task-cli.py list
```
Filter tasks by status:
```bash
python task-cli.py list todo
python task-cli.py list in-progress
python task-cli.py list done

```

## License

This project is licensed under the **MIT License**.