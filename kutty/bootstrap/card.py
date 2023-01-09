"""Bootstrap Card component.

There is a `Card` low-level component that doesn't have anything by itself but
needs to be populated by hand with `.add_body()`, `.add_header()`,
`.add_footer()`, in addition to `.add()`.

This module also exposes the higher-level components built on top of `Card`.
It is recommended to use them directly.
Higher-level components: `SimpleCard`

Example usage:

```python
from kutty.bootstrap import SimpleCard

card = SimpleCard(
    title="Foo", subtitle="More about foo", text="Foo is spam, ham and eggs."
)
card.body << Link("Go somewhere", href="#")
```

Header and footer elements are automatically added, and can be populated with
`<<` or with text during initialization.

```python
from kutty.bootstrap import SimpleCard

# either like this:
card = SimpleCard(header="Featured")

# or like this:
card = SimpleCard()
card.header << "Featured"
```

Footer can be accessed analogously with `.footer`.

Content can be added to the "top" and "bottom" of the card by adding to
`card.top` and `card.bottom`. `card.top` is (by default) a `div` between
the header and body, and `card.bottom` is (by default) a `div` between
the body and footer.

```python
from kutty import Image
from kutty.bootstrap import SimpleCard

card = SimpleCard()
card.top << Image("https://example.com/image.jpeg")
```

Additionally, any image added to `card.top` will be injected with the class
`card-img-top`. This gives the image rounded top corners. The behaviour is
analogous when an image is added to the bottom of the card, the class added
is `card-img-bottom`.

For advanced usage, `Card` must be used instead of `SimpleCard`. This allows
more flexibility with `card.add_header`, `card.add_footer`, `card.add_body`,
and `card.add`.

For example, to create a list group inside an empty card, you can write:

```python
from kutty import html as h
from kutty.bootstrap import SimpleCard

card = Card(
    h.ul(class_="list-group list-group-flush")
      .add(h.li(class_="list-group-item", _content="An item"))
      .add(h.li(class_="list-group-item", _content="A second item"))
      .add(h.li(class_="list-group-item", _content="A third item"))
)
```
"""

from kutty import html, Link
from .base import BootstrapElement


class Card(BootstrapElement):
    TAG = "div"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_class("card")

    def add_header(self, *args, **kwargs):
        element = Header(*args, **kwargs)
        self.add(element)
        return element

    def add_body(self, *args, **kwargs):
        element = Body(*args, **kwargs)
        self.add(element)
        return element

    def add_footer(self, *args, **kwargs):
        element = Footer(*args, **kwargs)
        self.add(element)
        return element

class Header(BootstrapElement):
    TAG = "div"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_class("card-header")

class Body(BootstrapElement):
    TAG = "div"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_class("card-body")

    def add_title(self, content):
        if is_heading_element(content):
            element = content
        else:
            element = html.h5(content)
        element.add_class("card-title")
        super().add(element)
        return element

    def add_subtitle(self, content):
        if is_heading_element(content):
            element = content
        else:
            element = html.h6(content)
        element.add_class("card-subtitle text-muted")
        super().add(element)
        return element

    def add_text(self, content):
        if is_paragraph_element(content):
            element = content
        else:
            element = html.p(content)
        element.add_class("card-text")
        super().add(element)
        return element

    def add_link(self, content):
        if is_link_element(content):
            element = content
        else:
            element = Link(content)
        element.add_class("card-link")
        super().add(element)
        return element

class Footer(BootstrapElement):
    TAG = "div"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_class("card-footer")

class DefaultElement(html.HTMLElement):
    def __init__(
            self, *args,
            empty_condition=lambda self: not self.children, **kwargs):
        super().__init__(*args, **kwargs)
        self.empty_condition = empty_condition

    def render(self):
        if self.empty_condition(self):
            return ""
        else:
            return super().render()

class SimpleBody(Body):
    def __init__(self, *args, title=None, subtitle=None, text=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = self.add_title(title)
        self.subtitle = self.add_subtitle(subtitle)
        self.text = self.add_text(text)

    def add_title(self, title=None):
        if is_heading_element(title) or is_text(title):
            element = super().add_title(title)
        else:
            element = DefaultElement(_tag="h5", class_="card-title")
            self.add(element)
            if title is not None:
                element << title
        return element

    def add_subtitle(self, subtitle=None):
        if is_heading_element(subtitle) or is_text(subtitle):
            element = super().add_subtitle(subtitle)
        else:
            element = DefaultElement(_tag="h6", class_="card-subtitle text-muted")
            self.add(element)
            if subtitle is not None:
                element << subtitle
        return element

    def add_text(self, text=None):
        if is_paragraph_element(text) or is_text(text):
            element = super().add_text(text)
        else:
            element = DefaultElement(_tag="p", class_="card-text")
            self.add(element)
            if text is not None:
                element << text
        return element

    def add(self, element):
        if is_link_element(element):
            super().add_link(element)
            return self  # add should return self
        else:
            return super().add(element)

class Top(BootstrapElement):
    TAG = "div"

    def add(self, element):
        if is_image_element(element):
            element.add_class("card-img-top")
        return super().add(element)

class Bottom(BootstrapElement):
    TAG = "div"

    def add(self, element):
        if is_image_element(element):
            element.add_class("card-img-bottom")
        return super().add(element)

class SimpleCard(Card):
    def __init__(
            self,
            *args,
            header=None, top=None,
            body=None,
            bottom=None, footer=None,
            title=None, subtitle=None, text=None,
            **kwargs):
        super().__init__(*args, **kwargs)
        self.header = Header(header)
        self.top = Top(top)
        self.body = SimpleBody(body) if body else \
            SimpleBody(title=title, subtitle=subtitle, text=text) if title or subtitle or text else \
            SimpleBody()
        self.bottom = Bottom(bottom)
        self.footer = Footer(footer)

    def get_children(self):
        elements = [self.header, self.top, self.body, self.bottom,
                    *self.children, self.footer]
        for element in elements:
            if not self._is_empty_component(element):
                yield element

    def render(self):
        attrs = "".join(" " + self._render_attr(name, value) for name, value in self.attrs.items())
        children = self.get_children()
        content = "".join(c.render() for c in children)
        return f"<{self.TAG}{attrs}>{content}</{self.TAG}>"

    def _is_empty_component(self, thing):
        components = {self.header, self.top, self.body,
                      self.bottom, self.footer}
        return thing in components \
            and isinstance(thing, html.HTMLElement) \
            and not thing.children

def is_heading_element(thing):
    return isinstance(thing, html.HTMLElement) and \
            thing.TAG in {"h1", "h2", "h3", "h4", "h5", "h6"}

def is_link_element(thing):
    return isinstance(thing, html.HTMLElement) and \
            thing.TAG == "a"

def is_image_element(thing):
    return isinstance(thing, html.HTMLElement) and \
            thing.TAG == "img"

def is_paragraph_element(thing):
    return isinstance(thing, html.HTMLElement) and \
            thing.TAG == "p"

def is_text(thing):
    return isinstance(thing, str) or isinstance(thing, html.Text)
