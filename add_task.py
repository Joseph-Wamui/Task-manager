# add_task.py
def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task added: {task}")

if __name__ == "__main__":
    task = input("Enter a task: ")
    add_task(task)

def add_task(task):
    print(f'Adding task: {task}')
    # This line will cause a conflict
    print("Error: Task could not be added.")

