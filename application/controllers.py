from application import app
from flask import render_template, redirect, session, g, request, url_for
import forms

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def homepage():
	login_form = forms.LoginForm()
	query_engine = forms.QueryEngine()
	return render_template('homepage.html', login_form = login_form, query_engine = query_engine)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	login_form = forms.LoginForm()
	signup_form = forms.SignupForm()
	if login_form.validate_on_submit():
		redirect(url_for('index'))
	return render_template('signup.html', title = 'Sign Up', login_form = login_form, signup_form = signup_form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	login_form = forms.LoginForm()
	contact_form = forms.ContactForm()
	return render_template('contact.html', title = 'Contact Us', login_form = login_form, contact_form = contact_form)