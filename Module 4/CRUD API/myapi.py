from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/books_db"
mongo = PyMongo(app)

@app.route("/books", methods=["GET"])
def get_all_books():
    books = mongo.db.books.find()
    all_books = []
    for book in books:
        all_books.append({
            "id": str(book["_id"]),
            "book_name": book["book_name"],
            "author": book["author"],
            "publisher": book["publisher"]
        })
    return {"books": all_books}

@app.route("/book/<id>", methods=["GET"])
def get_book(id):
    book = mongo.db.books.find_one({"_id": id})
    if book:
        return {
            "id": str(book["_id"]),
            "book_name": book["book_name"],
            "author": book["author"],
            "publisher": book["publisher"]
        }
    else:
        return {"error": "book not found"}

@app.route("/book", methods=["POST"])
def add_book():
    book_name = request.json["book_name"]
    author = request.json["author"]
    publisher = request.json["publisher"]
    book_id = mongo.db.books.insert({
        "book_name": book_name,
        "author": author,
        "publisher": publisher
    })
    return {"id": str(book_id)}

@app.route("/book/<id>", methods=["PUT"])
def update_book(id):
    book_name = request.json["book_name"]
    author = request.json["author"]
    publisher = request.json["publisher"]
    mongo.db.books.update({"_id": id}, {
        "$set": {
            "book_name": book_name,
            "author": author,
            "publisher": publisher
        }
    })
    return {"message": "book updated"}

@app.route("/book/<id>", methods=["DELETE"])
def delete_book(id):
    mongo.db.books.delete_one({"_id": id})
    return {"message": "book deleted"}

if __name__ == "__main__":
    app.run()
