from . import db

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