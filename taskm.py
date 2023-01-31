class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"{self.name} ({status})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.complete()

    def view_tasks(self):
        for task in self.tasks:
            print(task)

# Example usage:
manager = TaskManager()
manager.add_task(Task("Go to the grocery store", "2022-01-01"))
manager.add_task(Task("Finish project report", "2022-01-15"))
manager.view_tasks() # Output: Go to the grocery store (Incomplete) Finish project report (Incomplete)
manager.complete_task("Go to the grocery store")
manager.view_tasks() # Output: Go to the grocery store (Completed) Finish project report (Incomplete)
