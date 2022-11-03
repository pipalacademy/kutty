"""Base HTML elements.
"""
from html import escape

class Text:
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

class Element:
    def __init__(self, content=None, **attrs):
        self.content = self.make_content(content)
        self.attrs = attrs

    def make_content(self, content):
        if isinstance(content, (Element, Text)):
            return content
        elif isinstance(content, str):
            return Text(content)
        elif content is None:
            return Text("")

    def render(self):
        attrs = "".join(" " + self._render_attr(name, value) for name, value in self.attrs.items())
        return f"<{self.TAG}{attrs}>{self.content.render()}</{self.TAG}>"

    def _render_attr(self, name, value):
        name = name.replace("_", "-").strip("-")
        value = escape(value)
        return f'{name}="{value}"'

class Div(Element):
    TAG = "div"

class P(Element):
    TAG = "p"

class Span(Element):
    TAG = "span"

class Strong(Element):
    TAG = "strong"

class Em(Element):
    TAG = "em"

class A(Element):
    TAG = "a"
