from application import app, mongo_client
from flask import render_template, redirect, session, g, request, url_for
import subprocess
import forms

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def homepage():
	login_form = forms.LoginForm(request.form)
	query_engine = forms.QueryEngine(request.form)

	return render_template('homepage.html', login_form = login_form, query_engine = query_engine)

@app.route('/results', methods=['GET', 'POST'])
def return_results():
	login_form = forms.LoginForm(request.form)
	matches = [{ 'user' : 'user 1'}, {'user' : 'user 2'}, {'user' : 'user 3'}, {'user' : 'user 4'}, {'user' : 'user 5'}, {'user' : 'user 6'}]
	return render_template('results.html', title = 'Search Results', matches = matches, login_form = login_form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	login_form = forms.LoginForm(request.form)
	signup_form = forms.SignupForm(request.form)
	messages = {'registered_user' : False}

	# TODO: CSRF validation
	if request.method == 'POST' and signup_form.validate():
		if not mongo_client.db.users.find({'username' : signup_form.username.data}):
			new_entry = {	
			'first_name' : signup_form.first_name.data,
			'last_name' : signup_form.last_name.data,
			'username' : signup_form.username.data,
			'password' : signup_form.password.data,
			'dartID' : signup_form.dartID.data,
			'email' : signup_form.email.data
			}
			mongo_client.db.users.insert(new_entry)
			messages['registered_user'] = True
		else:
			print mongo_client.db.users.find({'username' : signup_form.username.data})
			signup_form.errors['username'] = [u'Username already exists; please choose another one']

	return render_template('signup.html', title = 'Sign Up', login_form = login_form, signup_form = signup_form, messages = messages)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	login_form = forms.LoginForm(request.form)
	contact_form = forms.ContactForm(request.form)
	messages = {'submitted' : False}

	# TODO: CSRF validation
	if request.method == 'POST' and contact_form.validate():
		messages['submitted'] = True

	return render_template('contact.html', title = 'Contact Us', login_form = login_form, contact_form = contact_form, messages = messages)

@app.route('/profile', methods=['GET', 'POST'])
def profile():

	return render_template('profile.html')
