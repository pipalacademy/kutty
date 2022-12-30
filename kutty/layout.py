from . import html
from .components.navbar import Navbar
import json
from flask import make_response

BOOTSTRAP_CSS = "https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"


class Layout(html.Element):
    def __init__(self, title):
        self.title = title

        self.stylesheets = []
        self.javascripts = []

        self.add_stylesheet(BOOTSTRAP_CSS)

        self.navbar = Navbar(self.title)

    def add_stylesheet(self, link):
        self.stylesheets.append(link)

    def add_javascript(self, link):
        self.javascripts.append(link)

    def render(self, content=None):
        doc = html.Document()

        doc.head.add(html.title(self.title))

        for link in self.stylesheets:
            doc.head.add(html.link(rel="stylesheet", href=link))

        doc.body.add(self.navbar)
        container = html.div(class_="container")
        doc.body.add(container)
        if content:
            container.add(content)

        for link in self.javascripts:
            doc.body.add(html.script(src=link))

        return doc.render()

    def render_page(self, page):
        return self.render(page)

    def new_page(self, title):
        return Page(layout=self, title=title)

class Page(html.Element):
    def __init__(self, title):
        self.title = title
        self.content = html.div(class_="page")

        if self.title:
            self.add(html.h1(title))

    def add(self, element):
        self.content.add(element)

    def render(self):
        return self.content.render()

class RawPage:
    def __init__(self, content, content_type):
        self.content = content
        self.content_type = content_type

    def make_response(self):
        headers = {"content-type": self.content_type}
        return make_response(self.content, "200 OK", headers)

class JSONPage(RawPage):
    def __init__(self, data):
        super().__init__(json.dumps(data), "application/json")