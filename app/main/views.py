from flask import render_template
from . import main
from flask_login import login_required

#views
@login_required
@main.route('/')
def index():
    """
    function that return the index page and its data
    """
    return render_template('index.html')
    



   