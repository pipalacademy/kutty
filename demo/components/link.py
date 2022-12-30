from kutty import Page, Link, html

from _demo import Demo

page = Page("Link")

page << html.p("""
The Link component renders a link as <code>a</code> tag.
""")

code = """
from kutty import Link

link = Link("Google", href="https://google.com/")
"""

page << Demo(code, "link")
