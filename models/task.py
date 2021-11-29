from sqlalchemy.orm import relationship
from shared.models import db

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    tasklist_id = db.Column(db.Integer, db.ForeignKey('task_list.id'))


    def __init__(self, name, completed, tasklist_id):
        self.name = name
        self.completed = completed
        self.tasklist_id = tasklist_id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'completed': self.completed,
            'tasklist_id': self.tasklist_id
        }