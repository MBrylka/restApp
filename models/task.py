from shared.models import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, name, completed):
        self.name = name
        self.completed = completed

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'completed': self.completed
        }