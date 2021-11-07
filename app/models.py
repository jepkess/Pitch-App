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
    pass_secure=db.Column(db.String(255)) #column for password authentication.
    pitch=db.relationship('Pitch',backref='user',lazy="dynamic")

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

class Pitch(db.Model):
        id=db.Column(db.Integer, primary_key=True)
        pitch_title=db.Column(db.String(255)) 
        pitch_description=db.Column(db.String(255)) 
        posted=db.Column(db.DateTime,default=datetime.utcnow)
        user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
           
        def save(self):
          db.session.add(self)
          db.session.commit()

        
        def __repr__(self):
         return f'Comments: {self.pitch_title}'
        
class Post(db.Model):
     __tablename__ = 'posts'
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(255))
     user_id = db.Column(db.String(255))
     post = db.Column(db.String (255))
#      comment = db.relationship('Comment', backref='post', lazy='dynamic')
     category = db.Column(db.String(255))
     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#      likes = db.relationship('Likes', backref='post', lazy='dynamic')
#      dislikes = db.relationship('Dislikes', backref='post', lazy='dynamic')

     def save(self):
        db.session.add(self)
        db.session.commit()

     def delete(self):
        db.session.delete(self)
        db.session.commit()

     def __repr__(self):
        return f"Post Title: {self.title}"

# class Comment(db.Model):
#         __tablename__ ='comments'
#         id= db.Column(db.Integer, primary_key=True)
#         user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#         post_id=db.Column(db.Integer, db.ForeignKey('posts_id')) 
#         comment=db.Column(db.Text())

#         def save(self):
#          db.session.add(self)
#          db.session.commit()

#         @classmethod
#         def get_comments(cls, post_id):
#           comments = Comment.query.filter_by(post_id=post_id).all()
#           return comments 

       

#         def delete(self):
#           db.session.delete(self)
#           db.session.commit()

#         def __repr__(self):
#          return f'Comments: {self.comment}'       

        

   