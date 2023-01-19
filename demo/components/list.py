from kutty import Page, Link, html
from _demo import Demo

page = Page("List")

page << html.p("""
The List component create an ordered or unordered list.
""")

code = """
from kutty import List

page = List(["Apple", "Orange", "Mango"])
"""

page << Demo(code, "page")
