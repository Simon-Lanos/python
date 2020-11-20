import os
from flask import Flask, jsonify, json
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
app = Flask(__name__)

def load_json():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "books.json")
    return json.load(open(json_url))

books = load_json()

@app.route("/")
def index():
    template = env.get_template('index.html.tpl')
    return template.render()

@app.route("/hello/<name>")
def hello(name):
    template = env.get_template('page.html.tpl')
    return template.render(name=name)

# api
@app.route("/api/books/", methods=['GET'])
def api_books():
    return jsonify(books)

@app.route("/api/books/<isbn>", methods=['GET'])
def api_books_id(isbn):

    response = []
    for book in books:
        if book['isbn'] == isbn:
            return jsonify(book)

    return jsonify('Not found')

@app.route("/api/books/title/<title>", methods=['GET'])
def api_books_title(title):

    response = []
    for book in books:
        if book['title'] == title:
            return jsonify(book)

    return jsonify('Not found')


if __name__ == '__main__':
    app.run(debug=True)
