tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def show_tasks():
    for index, item in enumerate(tasks, 1):
        status = "Done" if item["completed"] else "Pending"
        print(f"{index}. {item['task']} - {status}")

add_task("Practice Python")
add_task("Learn React")
add_task("Build a project")

tasks[0]["completed"] = True
show_tasks()
