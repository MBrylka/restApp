from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from shared.models import db
from basicCrud import Tasks, TaskList, TaskListList

class FlaskApi():

    def __init__(self):     
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/tasks.db'
        db.init_app(self.app)
        
        with self.app.app_context():
            db.create_all()

    def addResource(self, res, endpoint):
        self.api.add_resource(res, endpoint) 

    def run(self):
        self.app.run()


if __name__ == '__main__':
    flaskApi = FlaskApi()
    flaskApi.addResource(Tasks, '/tasks/<task_id>')
    flaskApi.addResource(TaskList, '/tasks')
    flaskApi.addResource(TaskListList, '/taskLists')

    flaskApi.run()