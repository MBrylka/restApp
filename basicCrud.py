from flask_restful import reqparse, Resource
from shared.models import db
from models.task import Task
from modelmanagers.taskManager import taskManager

taskList = {
    'task1': {'name': 'create simple api', 'completed': False},
    'task2': {'name': 'create sqlAlchemy', 'completed': False},
    'task3': {'name': 'test in postman', 'completed': False}
}

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('completed')

class Tasks(Resource):

    def get(self, task_id):
        return taskManager.get(task_id)

    def delete(self, task_id):
        del taskList[task_id]
        return '', 204


class TaskList(Resource):
    def get(self):
        return taskManager.getAll()

    def put(self):
        args = parser.parse_args()
        return taskManager.add(args)

