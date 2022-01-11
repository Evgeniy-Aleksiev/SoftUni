from to_do_list.task import Task

class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []


    def add_task(self, new_task: Task):
        for task in self.tasks:
            if new_task.name == task.name:
                return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'


    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f'Completed task {task_name}'

        return f'Could not find task with the name {task_name}'


    def clean_section(self):
        compleated_count = 0

        for task in self.tasks:
            if task.completed:
                compleated_count += 1
                self.tasks.remove(task)

        return f'Cleared {compleated_count} tasks.'


    def view_section(self):
        information = f'Section {self.name}:'

        for task in self.tasks:
            information += '\n'
            information += task.details()
        return information

