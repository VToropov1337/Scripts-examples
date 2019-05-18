from flask import Flask
from config import Configuration
from posts.blueprint import posts2 #экземпляр класса блюпринт
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

app.register_blueprint(posts2, url_prefix='/blog') #передаем экземпляр класса блюпринт