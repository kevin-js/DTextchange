from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField, validators
from wtforms.widgets import TextArea

class LoginForm(Form):
	username = TextField('username', [validators.Required()])
	password = PasswordField('password')
	remember_me = BooleanField('remember_me', default = False)

class ContactForm(Form):
	name = TextField('name')
	subject = TextField('subject')
	message = TextField('message', widget = TextArea())
	submit = SubmitField('submission')

class SignupForm(Form):
	first_name = TextField('first_name')
	last_name = TextField('last_name')
	dartID = TextField('dartID')
	email = TextField('email')
	username = TextField('username')
	password = PasswordField('password')
	confirm_password = PasswordField('confirm password')
	submit = SubmitField('submission')

class QueryEngine(Form):
	query = TextField('query')