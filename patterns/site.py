from . import html


BOOTSTRAP_CSS = "https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"


class Site(html.Element):
    def __init__(self, title):
        self.title = title

        self.stylesheets = []
        self.javascripts = []

        self.add_stylesheet(BOOTSTRAP_CSS)

    def add_stylesheet(self, link):
        self.stylesheets.append(link)

    def add_javascript(self, link):
        self.javascripts.append(link)

    def render(self, content=None):
        doc = html.Document()

        doc.head.add(html.title(self.title))

        for link in self.stylesheets:
            doc.head.add(html.link(rel="stylesheet", href=link))

        if content:
            doc.body.add(content)

        for link in self.javascripts:
            doc.body.add(html.script(src=link))

        return doc.render()

    def new_page(self, title):
        return Page(site=self, title=title)

class Page(html.Element):

    def __init__(self, site, title):
        self.site = site
        self.title = title
        self.content = html.div(class_="page")

        if self.title:
            self.add(html.h1(title))

    def add(self, element):
        self.content.add(element)

    def render(self):
        return self.site.render(content=self.content)
