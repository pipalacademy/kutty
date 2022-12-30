from kutty import Layout, Link, html
from pathlib import Path

class DemoLayout(Layout):
    def render_page(self, page):
        content = html.div(class_="row", style="padding-top: 10px")
        left = html.div(class_="col-md-2")
        right = html.div(class_="col-md-10")
        right << page
        left << sidebar

        content << left
        content << right

        div = html.div()
        div << html.HTML(style)
        div << content

        return self.render(div)

def ListGroup(items):
    ul = html.ul(class_="list-group")
    for item in items:
        li = html.li(class_="list-group-item")
        li << item
        ul << li
    return ul


sidebar = html.div()

items = [
    Link("Home", href="/"),
    html.strong("Components")
]

components = sorted([p.stem for p in Path("demo/components").iterdir()])
items += [Link(c.title(), href="/components/" + c) for c in components]

sidebar << ListGroup(items)

layout = DemoLayout("Kutty Demo")

style = """
<style type="text/css">
.highlight {
    padding: 20px;
    margin: 20px 0px;
}
.highlight pre {
    margin: 0;
    line-height: inherit;
}

.demo {
    margin: 20px 0px;
    border: 1px solid #ddd;
    border-radius: 10px;
}
.demo-preview {
    padding: 20px;
    border-bottom: 1px solid #ddd;
}

.demo-code .highlight {
    margin: 0px;
}
</style>
"""

# TODO: replace this with local css
layout.add_stylesheet("https://pygments.org/_static/pygments.css")