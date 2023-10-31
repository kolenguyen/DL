from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    createdate = db.Column(db.DateTime, default=db.func.current_timestamp())

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'email': self.email,
    #         # 'password': self.password,
    #         'createdate': self.createdate
    #     }

    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self_):
        return f'<User (self.username)>'
    
class History(db.Model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    progress = db.Column(db.String(255), nullable=False)
    field = db.Column(db.String(255), nullable=False)

    user = db.relationship('User', backref=db.backref('histories', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'progress': self.progress,
            'field': self.field
        }
