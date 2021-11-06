from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin,db.Model): #de.model connect our class to the database and allow communication.
    __tablename__ = 'users'
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure=db.Column(db.String(255)) #column for password authentication.

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __rept__(self):
        return f'User {self.username}'

        