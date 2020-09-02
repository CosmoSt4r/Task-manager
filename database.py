from app import db
from datetime import datetime


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_text = db.Column(db.String(500))
    created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, task_text):
        self.task_text = task_text

    def __repr__(self):
        return f'<Task {self.task_id}>'
