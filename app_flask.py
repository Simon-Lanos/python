from flask import Flask
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('app_flask', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
app = Flask(__name__)

@app.route("/")
def index():
    template = env.get_template('index.html.tpl')
    return template.render()


@app.route("/hello/<name>")
def hello(name):
    template = env.get_template('page.html.tpl')
    return template.render(name=name)


if __name__ == '__main__':
    app.run(debug=True)
