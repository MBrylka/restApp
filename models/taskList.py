from sqlalchemy.orm import relationship
from shared.models import db

class TaskList(db.Model):
    __tablename__ = 'task_list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }