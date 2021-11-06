from flask import render_template
from . import main

#views

@main.route('/')
def index():
    """
    function that return the index page and its data
    """
    return render_template('index.html')

   