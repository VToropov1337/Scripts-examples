from flask import Blueprint
from flask import render_template

posts2 = Blueprint('posts',__name__,template_folder='templates')


@posts2.route('/') #так как зарегистрировали урл по другому адресу в апп.пи
def index():
	return render_template('posts/index.html') #так как блюпринт создан в папке posts, там создана папка templates (из 4 строки) и уже в ней файл html.