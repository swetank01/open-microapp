from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer)  # Assuming a user ID associated with tasks

    def serialize(self):
        return{
            'id' : self.id,
            'title' : self.title,
            'desc' : self.description,
            'completed' : self.completed,
            'user_id' : self.user_id
        }


    def __repr__(self):
        return f"<Task {self.title}>"