from pathlib import Path
from collections import Counter

DB = Path("todos.txt")


def read_todos():
    """Return a list of (done: bool, owner: str, text: str) tuples."""
    todos = []
    if DB.exists():
        for line in DB.read_text().splitlines():
            parts = line.split("\t")
            if len(parts) == 3:
                status, owner, text = parts
                done = status == "1"
                todos.append((done, owner, text))
            elif len(parts) == 2:
                # Older format: status + text
                status, text = parts
                done = status == "1"
                todos.append((done, "Unassigned", text))
            else:
                # Oldest format: just text
                todos.append((False, "Unassigned", line))
    return todos


def write_todos(todos):
    """Write a list of (done, owner, text) tuples back to the file."""
    lines = []
    for done, owner, text in todos:
        status = "1" if done else "0"
        lines.append(f"{status}\t{owner}\t{text}")
    DB.write_text("\n".join(lines))


def list_todos():
    """Print all tasks with indices, owner, and done/undone state."""
    todos = read_todos()
    if not todos:
        print("No tasks yet.")
        return

    print("\nCurrent tasks:")
    for i, (done, owner, text) in enumerate(todos, start=1):
        box = "[x]" if done else "[ ]"
        owner_label = f"@{owner}" if owner else "@Unassigned"
        print(f"{i}. {box} {owner_label} - {text}")

def format_entry(category, text):
    """Return the task text with an optional [category] prefix."""
    if category:
        return f"[{category}] {text}"
    return text


def list_by_owner(owner):
    """Print tasks filtered by owner."""
    todos = read_todos()
    filtered = [
        (i, done, text)
        for i, (done, task_owner, text) in enumerate(todos, start=1)
        if task_owner.lower() == owner.lower()
    ]
    if not filtered:
        print(f"No tasks for {owner}.")
        return

    print(f"\nTasks for {owner}:")
    for index, done, text in filtered:
        box = "[x]" if done else "[ ]"
        print(f"{index}. {box} {text}")


def add(todo, owner):
    todos = read_todos()
    if not owner:
        owner = "Unassigned"
    todos.append((False, owner, todo))
    write_todos(todos)
    print(f"Added: {todo} (owner: {owner})")
    print(f"Total todos: {len(todos)}")


def mark_done(index):
    todos = read_todos()
    if not (1 <= index <= len(todos)):
        print("Invalid task number.")
        return
    done, owner, text = todos[index - 1]
    todos[index - 1] = (True, owner, text)
    write_todos(todos)
    print(f"Marked as done: {text} (owner: {owner})")


def delete(index):
    todos = read_todos()
    if not (1 <= index <= len(todos)):
        print("Invalid task number.")
        return
    done, owner, text = todos.pop(index - 1)
    write_todos(todos)
    print(f"Deleted: {text} (owner: {owner})")


def show_summary():
    """Show how many tasks each owner has (done / total)."""
    todos = read_todos()
    if not todos:
        print("No tasks yet.")
        return

    total_per_owner = Counter()
    done_per_owner = Counter()

    for done, owner, _ in todos:
        if not owner:
            owner = "Unassigned"
        total_per_owner[owner] += 1
        if done:
            done_per_owner[owner] += 1

    print("\nSummary by owner:")
    for owner in sorted(total_per_owner.keys()):
        total = total_per_owner[owner]
        done = done_per_owner[owner]
        print(f"{owner}: {done}/{total} done")


def main():
    while True:
        print("\n--- TODO manager ---")
        list_todos()
        print("\nOptions:")
        print("1) Add task")
        print("2) Mark task as done")
        print("3) Delete task")
        print("4) List tasks for specific owner")
        print("5) Show summary by owner")
        print("q) Quit")
        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            owner = input("Owner (e.g. Loukas, Rana, George): ").strip()
            category = input("Category (optional, e.g. frontend, data, docs): ").strip()
            task = input("New task: ").strip()
            if not task:
                print("Nothing to add")
            else:
                entry = format_entry(category, task)
                add(entry, owner)
        elif choice == "2":
            num = input("Task number to mark as done: ").strip()
            if num.isdigit():
                mark_done(int(num))
            else:
                print("Please enter a valid number.")
        elif choice == "3":
            num = input("Task number to delete: ").strip()
            if num.isdigit():
                delete(int(num))
            else:
                print("Please enter a valid number.")
        elif choice == "4":
            owner = input("Owner to filter by: ").strip()
            if owner:
                list_by_owner(owner)
            else:
                print("Please enter a name.")
        elif choice == "5":
            show_summary()
        elif choice == "q":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

