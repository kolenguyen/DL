from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    createdate = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            # 'password': self.password, 
            'createdate': self.createdate
        }

    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self_):
        return f'<User (self.username)>'
