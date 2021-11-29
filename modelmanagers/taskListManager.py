from modelmanagers.baseManager import BaseManager
from shared.models import db
from models.taskList import TaskList
from models.task import Task

class TaskListManager(BaseManager):
    
    def get(self, id):
        return TaskList.query.filter_by(id=id).first().serialize()

    def getAll(self):
        taskLists = TaskList.query.all()
        
        tasksListsSerialized = {
            'tasksLists': [
                {
                    'tasklist': taskList.serialize(), 
                    'tasks': [task.serialize() for task in Task.query.filter_by(tasklist_id=taskList.id).all()]
                } for taskList in taskLists
                ]}

        return tasksListsSerialized

    def add(self, args):
        name = args['name']
        print(name)
        taskList = TaskList(name)
        db.session.add(taskList)
        db.session.commit()

        return taskList.serialize()

taskListManager = TaskListManager()