from flask import render_template,redirect,url_for,abort,request
from . import main
from flask_login import login_required,current_user
from .forms import PitchForm,CommentsForm,UpdateProfile
from ..models import Pitches, Comments,User
from .. import db,photos

#views
@main.route('/')
def index():
    """
    function that return the index page and its data
    """
    return render_template('home.html')

@main.route('/newpitch', methods = ['POST','GET'])
@login_required
def newpitch():
    """function for creating new pitch
    """
    form=PitchForm()
   
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        description = form.description.data
        #updating pitch instance.

        new_pitch = Pitches(pitch_title=title, category=category, pitch_description=description)
        new_pitch.save_pitch()
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.single_pitch'))
    else: 
        all_pitches= Pitches.query.order_by(Pitches.posted).all()
       
        
    return render_template('newpitch.html',pitch_form= form, pitches=all_pitches)

@main.route('/pitch', methods=['POST','GET']) 
@login_required
def single_pitch():
    """
    function that get one pitch.
    """
   
    form= CommentsForm()
    if form.validate_on_submit():
            new_comment= form.comment.data
            user_id = current_user._get_current_object().id
            pitch_id = current_user._get_current_object().id
            new_comment= Comments(comment=new_comment,user_id=user_id,pitch_id=pitch_id)
            new_comment.save_comment()
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('main.single_pitch'))
    else:

        all_pitches= Pitches.query.order_by(Pitches.posted).all()
        comments=Comments.query.order_by(Comments.comment).all()
        
    
    return render_template('pitch.html', pitches=all_pitches,commentform=form,comments=comments)

#user profile function
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)        


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    add_comment_form = UpdateProfile()

    if add_comment_form.validate_on_submit():
        user.bio = add_comment_form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',add_comment_form =add_comment_form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    
    



   