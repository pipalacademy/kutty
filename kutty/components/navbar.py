from dataclasses import dataclass
from typing import Any

from .. import html

@dataclass
class NavEntry:
    element: Any
    url: str
    right: bool

class Navbar(html.Element):
    def __init__(self, title):
        self.title = title
        self.entries = []

    def add_link(self, element, url, right=False):
        entry = NavEntry(element=element, url=url, right=right)
        self.entries.append(entry)

    def render_branding(self):
        return html.a(self.title, class_="navbar-brand", href="/")

    def render_hamburger(self, id):
        return html.button(
            html.span(class_="navbar-toggler-icon"),
            class_="navbar-toggler",
            type="button",
            data_bs_toggle="collapse",
            data_bs_target=f"#{id}",
        )

    def render_entries(self, id):
        content = html.div(
            class_="collapse navbar-collapse",
            id=id,
        )

        left_entries = html.ul(class_="navbar-nav me-auto mb-2 mb-lg-0")
        right_entries = html.div(class_="d-flex")

        for entry in self.entries:
            if not entry.right:
                left_entries.add(
                    html.li(self.render_link(entry), class_="nav-item")
                )
            else:
                right_entries.add(self.render_link(entry))

        content.add(left_entries)
        content.add(right_entries)
        return content

    def render_link(self, entry):
        return html.a(entry.element, class_="nav-link", href=entry.url)

    def render(self):
        container = html.div(class_="container")
        container.add(self.render_branding())
        container.add(self.render_hamburger(id="navbar-content"))
        container.add(self.render_entries(id="navbar-content"))

        nav = html.nav(container, class_="navbar navbar-expand-lg bg-light")
        return nav.render()
