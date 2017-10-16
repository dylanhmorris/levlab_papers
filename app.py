from flask import Flask
from string import Template

app = Flask(__name__)

AUTHOR_PAGE_TEMPLATE = Template("""
<h1>All papers authored by ${author_name}!</h1>
""")

HOME_PAGE_TEMPLATE = Template("""
<h1>Welcome to the Levin Lab paper repository</h1>
""")



@app.route("/")
def homepage():
    return HOME_PAGE_TEMPLATE.substitute()

@app.route("/<author_name>")
def author_page(author_name):
    return AUTHOR_PAGE_TEMPLATE.substitute(author_name=author_name)


if __name__ == '__main__':
    app.run()
