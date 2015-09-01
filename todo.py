from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from cement.core import handler

import arrow

from db_handler import add_task, list_tasks, delete_task


class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = "Don't forget important tasks!"
        arguments = [
            (['extra_arguments'], dict(action='store', nargs='*')),
            ]

    @expose(help="Add task")
    def add(self):
        name = self.app.pargs.extra_arguments[0]
        description = self.app.pargs.extra_arguments[1]
        add_task(name, description)
        print("Task: " + name + " added!")
        
    @expose(help="Delete task")
    def delete(self):
        task = self.app.pargs.extra_arguments[0]
        delete_task(task)
        print("Task deleted!")

    @expose(help="List all tasks")
    def tasks(self):
        for task in list_tasks():
            converted_time = arrow.get(task.created_at)
            print(task.task_name, task.task_description, converted_time.humanize())


class TodoApp(CementApp):
    class Meta:
        label = 'todoapp'
        base_controller = 'base'
        handlers = [BaseController]


with TodoApp() as app:
    app.run()
