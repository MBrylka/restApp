from modelmanagers.baseManager import BaseManager
from shared.models import db
from models.task import Task

class TaskManager(BaseManager):
    
    def get(self, id):
        return Task.query.filter_by(id=id).first().serialize()

    def getAll(self):
        tasks = Task.query.all()
        tasksSerialized = {'tasks': [task.serialize() for task in tasks]}

        return tasksSerialized

    def add(self, args):
        name = args['name']
        completed = eval(args['completed'])
        tasklist_id = eval(args['tasklist_id'])
        
        task = Task(name, completed, tasklist_id)
        db.session.add(task)
        db.session.commit()

        return task.serialize()

taskManager = TaskManager()