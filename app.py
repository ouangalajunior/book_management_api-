from flask import Flask
from flask_smorest import Api
from resources.library import blue_print_library as LibraryBluePrint
from resources.book import blue_print_book as BookBluePrint





app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Libraries and Books REST API"
app.config["API_VERSION"] = "V1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"



api=Api(app)

api.register_blueprint(LibraryBluePrint)
api.register_blueprint(BookBluePrint)