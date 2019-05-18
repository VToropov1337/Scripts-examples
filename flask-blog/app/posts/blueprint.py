from flask import Blueprint
from flask import render_template

posts = Blueprint('posts',__name__,template_folder='templates')


@posts.route('/') #так как зарегистрировали урл по другому адресу в апп.пи
def index():
	return render_template('posts/index.html')