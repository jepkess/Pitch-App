from sqlalchemy.orm import backref
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin,db.Model): #de.model connect our class to the database and allow communication.
    __tablename__ = 'users'
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pitches=db.relationship('Pitches',backref='user',lazy="dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure=db.Column(db.String(255)) #column for password authentication.
    comments=db.relationship('Comments',backref='user',lazy="dynamic")
   

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

        

class Pitches(db.Model):
        __tablename__ = 'pitches'
        id=db.Column(db.Integer, primary_key=True)
        pitch_title=db.Column(db.String(255)) 
        pitch_description=db.Column(db.String(255))
        category = db.Column(db.String)
        comment=db.relationship('Comments',backref='pitch',lazy="dynamic")
        posted=db.Column(db.DateTime,default=datetime.utcnow)
        user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
           
        def save_pitch(self):

          db.session.add(self)
          db.session.commit()

        @classmethod
        def get_pitches(cls,id):
                pitches =Pitches.query.filter_by(pitch_id=id).all()
                return pitches

        
        def __repr__(self):
         return f'Comments: {self.pitch_title}'

class Comments(db.Model):
    __tablename__ = 'comments'
    id= db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text())
    user_id= db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    pitch_id= db.Column(db.Integer,db.ForeignKey('pitches.id'), nullable=False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_comment(cls,pitch_id):
        comment = Comments.query.filter_by(pitch_id=pitch_id).all()
        return comment

    def __repr__(self):
        return f'Comments: {self.comment}'
       
 

