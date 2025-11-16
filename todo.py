from pathlib import Path

DB = Path("todos.txt")


def read_todos():
    """Return a list of (done: bool, text: str) tuples."""
    todos = []
    if DB.exists():
        for line in DB.read_text().splitlines():
            if "\t" in line:
                status, text = line.split("\t", 1)
                done = status == "1"
                todos.append((done, text))
            else:
                # Backwards compatibility: old format without status
                todos.append((False, line))
    return todos


def write_todos(todos):
    """Write a list of (done, text) tuples back to the file."""
    lines = []
    for done, text in todos:
        status = "1" if done else "0"
        lines.append(f"{status}\t{text}")
    DB.write_text("\n".join(lines))


def list_todos():
    """Print all tasks with indices and done/undone state."""
    todos = read_todos()
    if not todos:
        print("No tasks yet.")
        return

    print("\nCurrent tasks:")
    for i, (done, text) in enumerate(todos, start=1):
        box = "[x]" if done else "[ ]"
        print(f"{i}. {box} {text}")


def add(todo):
    todos = read_todos()
    todos.append((False, todo))
    write_todos(todos)
    print(f"Added: {todo}")


def mark_done(index):
    todos = read_todos()
    if not (1 <= index <= len(todos)):
        print("Invalid task number.")
        return
    done, text = todos[index - 1]
    todos[index - 1] = (True, text)
    write_todos(todos)
    print(f"Marked as done: {text}")


def delete(index):
    todos = read_todos()
    if not (1 <= index <= len(todos)):
        print("Invalid task number.")
        return
    done, text = todos.pop(index - 1)
    write_todos(todos)
    print(f"Deleted: {text}")


def main():
    while True:
        print("\n--- TODO manager ---")
        list_todos()
        print("\nOptions:")
        print("1) Add task")
        print("2) Mark task as done")
        print("3) Delete task")
        print("q) Quit")
        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            task = input("New task: ").strip()
            if task:
                add(task)
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
        elif choice == "q":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

