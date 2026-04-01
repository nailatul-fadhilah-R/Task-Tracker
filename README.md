# Task Tracker CLI

A simple Command Line Interface (CLI) application to manage your to-do list, built with Python.

## Features
- Add, Update, and Delete tasks.
- Mark tasks as **In Progress** or **Done**.
- Filter tasks by status (todo, in-progress, done).
- Persistent storage using a local JSON file.

## How to Use

1. **Add a new task**
   ```bash
   python task_cli.py add "Buy groceries"
   
2. **List all tasks**
   ```bash
   python task_cli.py list

3. **Update a task**
   ```bash
   python task_cli.py update 1 "Buy groceries and cook dinner"

4. **Mark status**
   ```bash
   python task_cli.py mark-in-progress 1
   python task_cli.py mark-done 1

5. **List by status**
   ```bash
   python task_cli.py list done

## Why this works
- sys.argv: This is a list in Python that contains all the command-line arguments. sys.argv[0] is the script name, sys.argv[1] is the command (like "add"), and so on.
- JSON Persistence: Every time you run a command, the script reads the current state of tasks.json, modifies the list in memory, and overwrites the file with the new data.
- Error Handling: I added basic checks to ensure that if you try to update a task ID that doesn't exist, the app won't crash; it will simply tell you the ID wasn't found.

## Project Page
https://roadmap.sh/projects/task-tracker
