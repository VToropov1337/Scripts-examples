from flask import Blueprint
from flask import render_template
from models import Post, Tag

posts = Blueprint('posts',__name__,template_folder='templates')


@posts.route('/') #так как зарегистрировали урл по другому адресу в апп.пи
def index():
	all_posts = Post.query.all()
	return render_template('posts/index.html',objects=all_posts) #так как блюпринт создан в папке posts, там создана папка templates (из 4 строки) и уже в ней файл html.

#localhost/blog/post
@posts.route('/<slug>')
def post_detail(slug):
	post = Post.query.filter(Post.slug==slug).first()
	tags = post.tags
	return render_template('posts/post_detail.html',post_object=post, tags = tags)
#localhost/blog/tag/python
@posts.route('/tag/<slug>')
def tag_detail(slug):
	tag = Tag.query.filter(Tag.slug==slug).first()
	posts = tag.posts.all() #чтобы получить список всех постов
	return render_template('posts/tag_detail.html', tag=tag, posts=posts)



