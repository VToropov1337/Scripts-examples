from flask import Blueprint
from flask import render_template
from models import Post

posts = Blueprint('posts',__name__,template_folder='templates')


@posts.route('/') #так как зарегистрировали урл по другому адресу в апп.пи
def index():
	all_posts = Post.query.all()
	return render_template('posts/index.html',objects=all_posts) #так как блюпринт создан в папке posts, там создана папка templates (из 4 строки) и уже в ней файл html.

#localhost/blog/post
@posts.route('/<slug>')
def post_detail(slug):
	post = Post.query.filter(Post.slug==slug).first()
	return render_template('posts/post_detail.html',post_object=post)

