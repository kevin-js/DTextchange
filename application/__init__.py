from flask import Flask
from flask.ext.pymongo import PyMongo
import forms

app = Flask(__name__)
app.config.from_object('config')
# temporary run on localhost
mongo_client = PyMongo(app)

from application import views