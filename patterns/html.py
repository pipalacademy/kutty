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
    def __init__(self, content=None, **attrs):
        self.children = []
        self.attrs = attrs
        if content is not None:
            self.add(content)

    def add(self, content):
        if isinstance(content, str):
            content = Text(content)
        self.children.append(content)

    def render(self):
        attrs = "".join(" " + self._render_attr(name, value) for name, value in self.attrs.items())
        if self.children:
            content = "".join(c.render() for c in self.children)
            return f"<{self.TAG}{attrs}>{content}</{self.TAG}>"
        else:
            return f"<{self.TAG}{attrs} />"

    def _render_attr(self, name, value):
        name = name.replace("_", "-").strip("-")
        value = escape(value)
        return f'{name}="{value}"'

def make_element(tag):
    class Node(HTMLElement):
        TAG = tag

    Node.__name__ = tag
    return Node


div = make_element("div")
p = make_element("p")

br = make_element("br")
img = make_element("img")
a = make_element("a")

span = make_element("span")
strong = make_element("strong")
em = make_element("em")

