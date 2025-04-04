import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from db import libraries


blue_print_library = Blueprint("libraries", __name__, description = "Operations on libraries")


@blue_print_library.route("/library/<string:library_id>")
class Library(MethodView):
    def get(self, library_id):
        
        try:
            return libraries[library_id]
        except KeyError:
            return {"message": "Library not found"}, 404
    
    def delete(self, library_id):
        try:
            del libraries[library_id]
            return {"message": "Library deleted"}
        except KeyError:
            return {"message": "Library not found"}, 404
        
    def put(self, library_id):
        library_data = request.get_json()
        if "name" not in library_data :
            return {"message": "Bad request. Ensure 'name' is included in the JSON payload"}, 400
        try:
            library = libraries[library_id]
            library |= library_data
            return library
        except KeyError:
            return {"message": "Library not found"}, 404
        
        

@blue_print_library.route("/library")
class Libraries(MethodView):
    def get(self):
        return {"libraries": list(libraries.values())}
    
    def post(self):
        library_data = request.get_json()
        library_id = uuid.uuid4().hex
        library = {**library_data, "id": library_id}
        libraries[library_id] = library
    
        return library, 201
    