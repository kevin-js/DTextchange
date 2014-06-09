from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField

class LoginForm(Form):
	username = TextField('username', default = 'username')
	password = PasswordField('password', default = 'password')
	remember_me = BooleanField('remember_me', default = False)

class QueryEngine(Form):
	query = TextField('query')