from app import app
from flask import render_template

@app.route('/')
def index():
	name = 'Vladimir'
	return render_template('index.html', n=name)

@app.route('/about')
def about():
	return render_template('about.html')