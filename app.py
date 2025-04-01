from flask import Flask, request
from db import libraries, books

app = Flask(__name__)


libraries = [
    {
        "name": "My Bibliotheque",
        "books": [
            {
                "title": "Mon book",
                "author": "Osee Junior",
                "year": 1999
            }
        ]
    }
]



@app.get("/library")
def get_libraries():
    return {"libraries": libraries}

@app.post("/library")
def create_library():
    request_data = request.get_json()
    new_library = {"name": request_data["name"], "books":[]}
    libraries.append(new_library)
    return new_library, 201


#Create book
@app.post("/library/<string:name>/book")
def create_book(title):
    request_data = request.get_json()
    for library in libraries:
        if library["name"] == name:
            new_book = {"title": request_data["title"], "author": request_data["author"], "year": request_data["year"]}
            store["books"].append(new_book)
            return new_book,201
    return {"message": "Library not found"}, 404


@app.get("/library/<string:name>")
def get_library(name):
    for library in libraries:
        if library["name"] == name:
            return library
    return {"message": "Library not found"}, 404


@app.get("/library/<string:name>/book")
def get_book_in_library(name):
    for library in libraries:
        if library["name"] == name:
            return {"books": library["books"]}
    return {"message": "Library not found"}, 404
    