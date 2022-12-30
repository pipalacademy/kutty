"""Base HTML elements.
"""
from html import escape

class Element:
    """Base class for all elements in patterns.
    """
    def render(self) -> str:
        """Renders the element."""
        raise NotImplementedError()

    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    def __str__(self):
        return self.render()

    # The << operator
    def __lshift__(self, component):
        return self.add(component)

    def add(self, component):
        raise Exception(f"Adding child elements is not supported for {self.__class__.__name__}")

class Text(Element):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

class HTML(Element):
    """Raw HTML"""
    def __init__(self, html):
        self.html = html

    def render(self):
        return self.html

class HTMLElement(Element):
    """Base class for all plain html elements.
    """
    KIND = "normal"

    def __init__(self, _content=None, _tag=None, **attrs):
        self.children = []
        self.attrs = attrs
        if _content is not None:
            self.add(_content)

        # special case to support arbitrary tags
        if _tag:
            self.TAG = _tag

    def __repr__(self):
        return f"<Tag:{self.TAG}>"

    def add(self, content):
        if not isinstance(content, Element):
            content = Text(str(content))
        self.children.append(content)

        # Result self to allow chaining of methods
        return self

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

def tag(name, *children, **kwargs):
    e = HTMLElement(_tag=name, **kwargs)
    for child in children:
        e.add(child)
    return e

div = make_element("div")
p = make_element("p")
pre = make_element("pre")
nav = make_element("nav")
ul = make_element("ul")
li = make_element("li")

br = make_element("br", kind="void")
img = make_element("img", kind="void")
a = make_element("a")
button = make_element("button")

span = make_element("span")
strong = make_element("strong")
em = make_element("em")
h1 = make_element("h1")
h2 = make_element("h2")
h3 = make_element("h3")
h4 = make_element("h4")
h5 = make_element("h5")

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
