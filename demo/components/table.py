from kutty import Page, Table, Code, html

from _demo import Demo

page = Page("Table")

page << html.p("""
The table component renders an HTML table.

You can specify the columns and data when
creating the table or add rows after creating it.
""")

code = """
from kutty import Table
table = Table(columns=["Name", "Price", "Quantity", "Amount"])
table.add_row(["Apple", 10, 5, 50])
table.add_row(["Banana", 2, 3, 6])
"""

page << Demo(code, "table")
