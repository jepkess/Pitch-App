from . import db

class User(db.Model): #de.model connect our class to the database and allow communication.
    __tablename__ = 'users'
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))

    def __rept__(self):
        return f'User {self.username}'