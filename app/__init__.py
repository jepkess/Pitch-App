from flask import Flask
#initializing the application
app=Flask(__name__)

from app.main import views

