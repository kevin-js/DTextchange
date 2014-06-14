from application import app, mongo_client
from flask import render_template, redirect, session, g, request, url_for
import forms

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def homepage():
	login_form = forms.LoginForm()
	query_engine = forms.QueryEngine()
	return render_template('homepage.html', login_form = login_form, query_engine = query_engine)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	login_form = forms.LoginForm()
	signup_form = forms.SignupForm()
	successful_register = False
	if request.method == 'POST' and signup_form.validate():
		mongo_client.db.users.insert({	'first_name' : signup_form.first_name.data,
										'last_name' : signup_form.last_name.data,
										'username' : signup_form.username.data,
										'password' : signup_form.password.data,
										'dartID' : signup_form.dartID.data,
										'email' : signup_form.email.data
										})
		successful_register = True
	return render_template('signup.html', title = 'Sign Up', login_form = login_form, signup_form = signup_form, register_state = successful_register)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	login_form = forms.LoginForm()
	contact_form = forms.ContactForm()
	messages = {'submitted' : False}
	if request.method == 'POST':
		messages = {'submitted': True}
		print 'got here'
	return render_template('contact.html', title = 'Contact Us', login_form = login_form, contact_form = contact_form, messages = messages)