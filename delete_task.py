# delete_task.py
def delete_task(task):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        with open("tasks.txt", "w") as file:
            for t in tasks:
                if t.strip("\n") != task:
                    file.write(t)
        print(f"Task deleted: {task}")
    except FileNotFoundError:
        print("No tasks found!")

if __name__ == "__main__":
    task = input("Enter a task to delete: ")
    delete_task(task)
