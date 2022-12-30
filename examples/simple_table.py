from flask import Flask
from kutty import Layout, Page, Table

app = Flask(__name__)
layout = Layout("Table Demo")

@app.route("/")
def index():
    table = Table(columns=["Name", "Price", "Quantity", "Amount"])
    table.add_row(["Apple", 10, 5, 50])
    table.add_row(["Banana", 2, 3, 6])

    page = Page("Table demo")
    page.add(table)

    return layout.render_page(page)

if __name__ == "__main__":
    app.run()

