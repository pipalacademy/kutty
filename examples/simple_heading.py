from flask import Flask

from patterns import Site, Page
from patterns import html


site = Site("FooBar")
site.navbar.add_link("foo", "/foo")
site.navbar.add_link("login", "/login", right=True)

page = site.new_page("Hello world")

app = Flask(__name__)

@app.route("/")
def index():
    return page.render()

if __name__ == "__main__":
    app.run()
