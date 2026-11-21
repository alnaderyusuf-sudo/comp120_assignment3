"""Simple task list for COMP120 Assignment 3."""

from pathlib import Path

TASK_FILE = Path("tasks.txt")


def add_task(task, file_path=TASK_FILE):
    task = task.strip()
    if not task:
        return False
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(task + "\n")
    return True


def read_tasks(file_path=TASK_FILE):
    if not Path(file_path).exists():
        return []
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def main():
    while True:
        print("\nTask List")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Exit")
        choice = input("Choose 1, 2, or 3: ").strip()

        if choice == "1":
            task = input("Enter a task: ")
            if add_task(task):
                print("Task added.")
            else:
                print("Please enter a task name.")
        elif choice == "2":
            tasks = read_tasks()
            if not tasks:
                print("No tasks added yet.")
            else:
                for number, task in enumerate(tasks, 1):
                    print(f"{number}. {task}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
