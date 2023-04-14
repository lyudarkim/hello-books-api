from flask import Blueprint, jsonify


class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description


books = [
    Book(1, "Book A", "Description A"),
    Book(2, "Book B", "Description B"),
    Book(3, "Book C", "Description C"),
]

hello_world_bp = Blueprint("hello_world", __name__)
books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description,
        })
    return jsonify(books_response), 200

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_beautiful_world = "Hello, World!"
    return my_beautiful_world, 200

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "CheezItMan",
        "message": "Need more Cheez!",
        "hobbies": ["Snacks", "Coding", "Gardening"]
    }, 200

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"] + new_hobby
    return response_body