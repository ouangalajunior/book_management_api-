from flask import Flask, request
from db import libraries, books

import uuid

app = Flask(__name__)




#Get libraries
@app.get("/library")
def get_libraries():
    return {"libraries": list(libraries.values())}

#Create library
@app.post("/library")
def create_library():
    library_data = request.get_json()
    library_id = uuid.uuid4().hex
    library = {**library_data, "id": library_id}
    libraries[library_id] = library
    
    return library, 201

#Get a library based on library id
@app.get("/library/<string:library_id>")
def get_library(library_id):
    try:
        return libraries[library_id]
    except KeyError:
        return {"message": "Library not found"}, 404

#Delete a library based on library id    
@app.delete("/library/<string:library_id>")
def delete_library(library_id):
    try:
        del libraries[library_id]
        return {"message": "Library deleted"}
    except KeyError:
        return {"message": "Library not found"}, 404

#Update library
@app.put("/library/<string:library_id>")
def update_library(library_id):
    library_data = request.get_json()
    if "name" not in library_data :
        return {"message": "Bad request. Ensure 'name' is included in the JSON payload"}, 400
    try:
        library = libraries[library_id]
        library |= library_data
        return library
    except KeyError:
        return {"message": "Library not found"}, 404

#Create book
@app.post("/book")
def create_book():
    book_data = request.get_json()
    if book_data["library_id"] not in libraries:
        return {"message": "Library not found"}, 404
    book_id = uuid.uuid4().hex
    book = {**book_data, "id": book_id}
    books[book_id] = book
    return book, 201

#Get a list of books
@app.get("/book")
def get_books():
    return {"books": list(books.values())}

#Delete a book
@app.delete("/book/<string:book_id>")
def delete_book(book_id):
    try:
        del books[book_id]
        return {"message": "Book deleted"}
    except KeyError:
        return {"message": "Book not found"}, 404

#Get a book
@app.get("/book/<string:book_id>")
def get_book(book_id):
    try:
        return books[book_id]
    except KeyError:
        return {"message": "Book not found"}, 404

#Update book
@app.put("/book/<string:book_id>")
def update_book(book_id):
    book_data = request.get_json()
    if "title" not in book_data or "author" not in book_data or "year" not in book_data:
        return {"message": "Bad request. Ensure 'title', 'author', and 'year' are included in the JSON payload"}, 400
    try:
        book = books[book_id]
        book |= book_data
        return book
    except KeyError:
        return {"message": "Book not found"}, 404

    
    