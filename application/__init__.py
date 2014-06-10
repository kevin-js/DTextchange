from flask import Flask
import forms

app = Flask(__name__)
app.config.from_object('config')

from application import controllers