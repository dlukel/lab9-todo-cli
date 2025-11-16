# todo_cli

A starter command-line to-do list used in Lab 9 to learn Git.

## Overview

This is a simple terminal-based TODO manager.
Tasks are stored in a "todos.txt" file in the same folder and each task has:

- done/undone status
- an owner (e.g. Loukas, Rana, George)
- a text description

You can use it to keep track of tasks for your CSEN100 group project.

## How to run

1. Make sure you have Python 3 installed.
2. From the "todo_cli" folder, run:

   
->python3 todo.py
   

3. You will see the current tasks and a menu of options.

## Features

When you run the app, you will see a menu like:

- "1) Add task"
- "2) Mark task as done"
- "3) Delete task"
- "4) List tasks for specific owner"
- "5) Show summary by owner"
- "q) Quit"

### Add task

- Choose option "1".
- Enter the **owner** (e.g. "Loukas", "Rana", "George").
- Enter the **task description**.
- The app will:
  - Save the task with status “not done”.
  - Print "Added: … (owner: …)".
  - Print "Total todos: X" with the updated count.

If you leave the task description empty and just press Enter, the app prints:

> "Nothing to add"

and does **not** save anything.

### Mark task as done

- Choose option "2".
- Enter the **task number** shown in the list.
- The app updates the task to done and prints a confirmation.

### Delete task

- Choose option "3".
- Enter the **task number**.
- The app removes the task from the file.

### List tasks for specific owner

- Choose option "4".
- Enter an owner name (e.g. "Loukas").
- The app prints only the tasks assigned to that owner, with their indices and done/undone status.

### Summary by owner

- Choose option "5".
- The app prints, for each owner:

  OwnerName: done/total done

This lets you quickly see who has completed how many tasks.

## Data format

Tasks are stored in "todos.txt" in a simple tab-separated format:


status<TAB>owner<TAB>text

- "status" is "1" for done, "0" for not done.
- "owner" is the string you entered (or "Unassigned").
- "text" is the task description.

Older formats (without owner or status) are still supported and will be treated as "Unassigned" not-done tasks.

## Git and .gitignore

In this lab setup, "todos.txt" should **not** be committed to Git, because it is user-specific data.
Only the source files ("todo.py", "README.md", etc.) are tracked in version control.

