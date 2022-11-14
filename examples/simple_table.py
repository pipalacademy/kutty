from flask import Flask
from patterns import Layout, Table


app = Flask(__name__)
layout = Layout("Foo Table")


@app.route("/")
def index():
    table = Table(columns=["Name", "Price", "Quantity", "Amount"])
    table.add_row(["Apple", 10, 5, 50])
    table.add_row(["Banana", 2, 3, 6])

    page = layout.new_page("Table demo")
    page.add(table)

    return page.render()
