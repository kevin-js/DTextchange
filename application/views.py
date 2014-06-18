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

	if request.method == 'POST':# login_form.validate():
		user_info = None
		for entry in mongo_client.db.users.find({'username' : login_form.username.data}):
			user_info = entry
			break
		if not user_info:
			login_form.errors['username'] = [u'User not found!']
		elif login_form.password.data != user_info['password']:
			login_form.errors['password'] = [u'Incorrect password, please try again']
		else:	
			session['logged_in'] = True
			session['user'] = user_info['username']

	return render_template('homepage.html', login_form = login_form, query_engine = query_engine)

@app.route('/results', methods=['GET', 'POST'])
def return_results():
	login_form = forms.LoginForm(request.form)
	matches = [{'name': 'Test User',
				'email': 'test@test.com',
				'class': '2016',
				'profile_picture': url_for('static', filename='img/default_prof_pic.png')},
				]
	return render_template('results.html', title = 'Search Results', matches = matches, login_form = login_form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	login_form = forms.LoginForm(request.form)
	signup_form = forms.SignupForm(request.form)
	messages = {'registered_user' : False}

	# TODO: CSRF validation
	if request.method == 'POST' and signup_form.validate():
		counter = 0
		for query_result in mongo_client.db.users.find({'username' : signup_form.username.data}):
			counter += 1

		if counter > 0:
			signup_form.errors['username'] = [u'Username already exists; please choose another one']
		
		else:
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
	user = {
				'name': 'Test User',
				'email': 'test@test.com',
				'class': '2016',
				'profile_picture': url_for('static', filename='img/default_prof_pic.png'),
				'phone' : '(123) 456-7890',
				'hinman' : 1234
			}
	return render_template('profile.html', user = user)

@app.route('/policies_and_information', methods=['GET', 'POST'])
def policies():
	return render_template('policies_and_information.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
	session['logged_in'] = False
	return redirect('/index')
