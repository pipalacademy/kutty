from flask import Flask

from patterns import Layout, Page


layout = Layout("FooBar")
layout.navbar.add_link("foo", "/foo")
layout.navbar.add_link("login", "/login", right=True)

app = Flask(__name__)

@app.route("/")
def index():
    # this sets the title, and an h1 tag automatically
    page = layout.new_page("Hello world")
    return page.render()

if __name__ == "__main__":
    app.run()
