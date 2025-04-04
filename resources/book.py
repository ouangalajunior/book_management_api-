import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from db import books
from db import libraries

blue_print_book = Blueprint("books", __name__, description="Operation on books")

@blue_print_book.route("/book/<string:book_id>")
class Book(MethodView):
    def get(self, book_id):
        
        try:
            return books[book_id]
        except KeyError:
            return {"message": "Book not found"}, 404
    
    def delete(self, book_id):
        try:
            del books[book_id]
            return {"message": "Book deleted"}
        except KeyError:
            return {"message": "Book not found"}, 404
    def put(self, book_id):
        book_data = request.get_json()
        if "title" not in book_data or "author" not in book_data or "year" not in book_data:
            return {"message": "Bad request. Ensure 'title', 'author', and 'year' are included in the JSON payload"}, 400
        try:
            book = books[book_id]
            book |= book_data
            return book
        except KeyError:
            return {"message": "Book not found"}, 404
        
@blue_print_book.route("/book")
class Books(MethodView):
    def get(self):
        return {"books": list(books.values())}
    
    def post(self):
        book_data = request.get_json()
        if book_data["library_id"] not in libraries:
            return {"message": "Library not found"}, 404
        book_id = uuid.uuid4().hex
        book = {**book_data, "id": book_id}
        books[book_id] = book
        return book, 201