from flask_restful import reqparse, Resource
from shared.models import db
from models.task import Task

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
        return Task.query.filter_by(id=task_id).first()

    def delete(self, task_id):
        del taskList[task_id]
        return '', 204

    def put(self, task_id):
        args = parser.parse_args()

        #task = {'name': args['name'], 'completed': args['completed']}
        #taskList[task_id] = task

        name = args['name']
        completed = bool(args['completed'])
        task = Task(name, completed)
        db.session.add(task)
        db.session.commit()
        
        print(task)

        return "ok", 201

class TaskList(Resource):
    def get(self):
        tasks = Task.query.all()
        return tasks

