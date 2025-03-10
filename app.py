from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': '1984',
        'autor': 'George Orwell',
        'year': 1949
    },
    {
        'id': 2,
        'title': 'To Kill a Mockingbird',
        'autor': 'Harper Lee',
        'year': 1960
    },
    {
        'id': 3,
        'title': 'The Great Gatsby',
        'autor': 'F. Scott Fitzgerald',
        'year': 1925
    },
    {
        'id': 4,
        'title': 'Pride and Prejudice',
        'autor': 'Jane Austen',
        'year': 1813
    },
    {
        'id': 5,
        'title': 'The Catcher in the Rye',
        'autor': 'J.D. Salinger',
        'year': 1951
    }
]

@app.route('/', methods=['GET'])
def home():
    return "API em Flask"

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book) # retorna o book
        # return jsonify({'message': 'Book not found'})
        
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
    book_data = request.get_json() 
    for ind,book in enumerate(books):
        if book.get('id') == id:
            books[ind].update(book_data)
            return jsonify(books[ind])
        
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book_by_id(id):
    for ind,book in enumerate(books):
        if book.get('id') == id:
            del books[ind]
    return jsonify(books)

app.run(port=5000, host='localhost', debug=True)