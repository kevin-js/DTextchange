from application import app
from flask import render_template
import forms

@app.route('/')
@app.route('/index')
def homepage():
	login_form = forms.LoginForm()
	query_engine = forms.QueryEngine()
	return render_template('homepage.html', login_form = login_form, query_engine = query_engine)

@app.route('/contact')
def contact():
	login_form = forms.LoginForm()
	return render_template('contact.html', title = 'Contact Us', login_form = login_form)