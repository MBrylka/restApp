from flask_restful import reqparse, Resource
from shared.models import db
from models.task import Task
from modelmanagers.taskManager import taskManager
from modelmanagers.taskListManager import taskListManager

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('completed')
parser.add_argument('tasklist_id')

class Tasks(Resource):

    def get(self, task_id):
        return taskManager.get(task_id)

    def delete(self, task_id):
        return '', 204


class TaskList(Resource):
    def get(self):
        return taskManager.getAll()

    def put(self):
        args = parser.parse_args()
        return taskManager.add(args)


class TaskListList(Resource):
    def get(self):
        return taskListManager.getAll()

    def put(self):
        args = parser.parse_args()
        return taskListManager.add(args)