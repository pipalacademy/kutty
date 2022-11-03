"""The Table component.

Sample Usage:

    from patterns import Table

    table = Table(columns=["Name", "Price", "Quantity", "Amount"])
    table.add_row(["Apple", 10, 5, 50])
    table.add_row(["Banana", 2, 3, 6])

Each row can also be constructed by adding one cell at a time.

    table = Table(columns=["Name", "E-Mail", "Website"])
    for user in users:
        row = table.add_row()
        row.add(user.name)
        row.add(user.email)
        row.add(user.website)
"""
from .. import html

class Table(html.Element):
    def __init__(self, data=None, *, columns=None):
        self.rows = [TableRow(row) for row in data or []]
        self.columns = columns

    def add_row(self, cells=None):
        """Adds a new row to the table and returns the TableRow object.
        """
        row = TableRow(cells=cells)
        self.rows.append(row)
        return row

    def render(self):
        if self.columns:
            rows = [TableRow(self.columns, header=True)] + self.rows
        else:
            rows = self.rows
        return html.tag("table", *rows, class_="table").render()

class TableRow(html.Element):
    def __init__(self, cells=None, header=False):
        self.cells = cells or []
        self.header = header

    def add(self, element):
        self.cells.append(element)

    def render(self):
        tagname = "th" if self.header else "td"
        tds = [html.tag(tagname, cell) for cell in self.cells]
        return html.tag("tr", *tds).render()
