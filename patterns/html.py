"""Base HTML elements.
"""
from html import escape

class Element:
    """Base class for all elements in patterns.
    """
    def render(self) -> str:
        """Renders the element."""
        raise NotImplementedError()

class Text(Element):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

class HTMLElement(Element):
    """Base class for all plain html elements.
    """
    KIND = "normal"

    def __init__(self, _content=None, **attrs):
        self.children = []
        self.attrs = attrs
        if _content is not None:
            self.add(_content)

    def add(self, content):
        if isinstance(content, str):
            content = Text(content)
        self.children.append(content)

    def render(self):
        attrs = "".join(" " + self._render_attr(name, value) for name, value in self.attrs.items())
        if self.KIND == "void":
            return f"<{self.TAG}{attrs}>"
        elif self.children:
            content = "".join(c.render() for c in self.children)
            return f"<{self.TAG}{attrs}>{content}</{self.TAG}>"
        else:
            return f"<{self.TAG}{attrs} />"

    def _render_attr(self, name, value):
        name = name.replace("_", "-").strip("-")
        value = escape(value)
        return f'{name}="{value}"'

def make_element(tag, kind="normal"):
    class Node(HTMLElement):
        TAG = tag
        KIND = kind

    Node.__name__ = tag
    return Node


div = make_element("div")
p = make_element("p")

br = make_element("br", kind="void")
img = make_element("img", kind="void")
a = make_element("a")

span = make_element("span")
strong = make_element("strong")
em = make_element("em")

html = make_element("html")
head = make_element("head")
body = make_element("body")
meta = make_element("meta", kind="void")
link = make_element("link", kind="void")
title = make_element("title")
script = make_element("script")

input = make_element("input", kind="void")

class Document(Element):
    def __init__(self):
        self.html = html()
        self.head = head()
        self.body = body()

        self.head.add(meta(charset="utf-8"))
        self.head.add(meta(name="viewport", content="width=device-width, initial-scale=1"))

        self.html.add(self.head)
        self.html.add(self.body)

    def render(self):
        return "<!DOCTYPE html>" + self.html.render()
