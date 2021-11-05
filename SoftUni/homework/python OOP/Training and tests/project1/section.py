class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        for current_task in self.tasks:
            if new_task.name == current_task.name:
                return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name):
        for current_task in self.tasks:
            if task_name == current_task.name:
                current_task.completed = True
                return f"Completed task {task_name}"

        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        removed_task_count = 0

        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                removed_task_count += 1

        return f"Cleared {removed_task_count} tasks."

    def view_section(self):
        result = f"Section {self.name}:"
        for task in self.tasks:
            result += '\n'
            result += task.details()

        return result