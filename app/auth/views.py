from flask import render_template
from . import auth

@auth.route('/login')
def login(): # login view function that renders the template file.
    return render_template('auth/login.html')