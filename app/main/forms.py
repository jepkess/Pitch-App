from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,TextAreaField,SubmitField
from wtforms import validators
from wtforms.validators import required

class PitchForm(FlaskForm):
    title=StringField('Pitch Title', [validators.DataRequired(message='Field required')])
    category=SelectField('Category',choices=[('PRAYER','PRAYER'),('NEWS','NEWS'),('RELATIONSHIP','RELATIONSHIP')])
    description=TextAreaField('Pitch Description', [validators.DataRequired(message='Field required')])
    submit=SubmitField('submit')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment',  [validators.DataRequired(message='Field required')])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',[validators.DataRequired(message='Field required')])
    submit = SubmitField('Submit')    
