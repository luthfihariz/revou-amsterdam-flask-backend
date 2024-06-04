from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# route
# views/function/ view function

@app.route("/", methods=["GET"]) # root
def index():
    return "Hello Flask 123!"

@app.route("/books", methods=["GET", "POST"])
def handle_books():
    if request.method == "POST":
        # Create book here
        return {"message": "Create a new book"}
    else:
        # Retrieve list of books here
        return {"message": "Return list of books"}

@app.route("/books-split", methods=["GET"])
def get_books():
    return jsonify({"message": "Return list of book"}), 200


@app.route("/books-split", methods=["POST"])
def add_book():
    jsonify({"message": "Add new book to the list!"}), 200


@app.route("/books-make-response", methods=["GET"])
def get_books_mr():
    response = make_response(jsonify({"message": "Return list of books"}), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route("/books-tuple", methods=["GET"])
def get_books_tuple():
    return (
        jsonify({"message": "Return list of books"}),
        200,
        {"Content-Type": "application/json"},
    )
