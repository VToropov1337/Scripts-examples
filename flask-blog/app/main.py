from app import app
import view #контроллер like
from app import db
from posts.blueprint import posts #экземпляр класса блюпринт

app.register_blueprint(posts, url_prefix='/blog') #передаем экземпляр класса блюпринт


if __name__ == '__main__':
	app.run()
