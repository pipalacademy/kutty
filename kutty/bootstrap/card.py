"""Bootstrap Card component.

There is a `Card` component that starts with a blank card and has a
`card.header`, `card.body` and `card.footer` that can be populated. They
are `Optional`s, meaning that they will be rendered only if they have
some content. This module also exposes constructors for components of
a Card, such as `CardHeader`, `CardBody`, and `CardFooter`.

The complete list of those components is:
- `CardHeader`
- `CardBody`
- `CardFooter`
- `CardTitle`
- `CardSubtitle`
- `CardText`
- `CardLink`
- `CardImageTop`
- `CardImageBottom`

They can be combined together as normal Kutty elements to make complex
elements in a composable manner.

It also takes some keyword arguments during initialization for simple
use cases.

Example usage:

```python
from kutty.bootstrap import Card

card = Card(
    title="Foo", subtitle="More about foo", text="Foo is spam, ham and eggs."
)
card.body.add_link("Go somewhere", "#")
```

Header and footer content can also be set during initialization, and are always
created as `Optional` containers. `card.header`, `card.footer`, and `card.body`
can be added to normally with `<<` operator or `.add()` method.

```python
from kutty.bootstrap import Card

# either like this:
card = Card(header="Featured")

# or like this, both are equivalent:
card = Card()
card.header << "Featured"
```

`footer` and `body` can be accessed similarly. Note that `CardBody` doesn't
have similar attributes. Title and subtitle cannot be set as attributes,
but should be done either with keyword arguments or with the `.add_title()`,
`.add_subtitle()` and `.add_text()` methods.

```python
from kutty.boostrap import Card

# this:
card = Card(title="Foo", text="Bar and baz.")

# is the same as:
card = Card()
card.body.add_title("Foo")
card.body.add_text("Bar and baz.")
```

There is also an `.add_link()` method like this that creates links with styles
that match with Bootstrap cards.

```python
from kutty.bootstrap import Card

card = Card()
card.body.add_link("foo", "/foo")
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

## Advanced usage

The components exposed by this module make it allow building complex cards
and retain the structure of the contents in the code.

```python
Card(
    CardHeader("Featured"),
    CardImageTop("/foo.jpeg", alt="Picture of Foo"),
    CardBody(
        CardTitle("Foo"),
        CardSubtitle("More about foo"),
        CardText("Foo is about spam, different from ham, and relates to eggs.")
    ),
)
```
"""

from kutty import html, Optional
from .base import BootstrapElement


class Card(BootstrapElement):
    TAG = "div"
    CLASS = "card"

    def __init__(
            self,
            *args,
            header=None,
            top_image=None,
            title=None, subtitle=None, text=None,
            footer=None,
            **kwargs):
        super().__init__(*args, **kwargs)

        self.header = Optional(CardHeader(header))
        self.top_image = CardImageTop(top_image)
        self.body = Optional(
            CardBody(
                **self._make_body_kwargs(
                    title=title, subtitle=subtitle, text=text
                )
            )
        )
        self.footer = Optional(CardFooter(footer))

        self.add(self.header)
        self.add(self.body)
        self.add(self.footer)

    def _make_body_kwargs(self, **kwargs):
        return {key: item for key, item in kwargs.items() if item is not None}

    def add_header(self, *args, **kwargs):
        element = CardHeader(*args, **kwargs)
        self.add(element)
        return element

    def add_body(self, *args, **kwargs):
        element = CardBody(*args, **kwargs)
        self.add(element)
        return element

    def add_footer(self, *args, **kwargs):
        element = CardFooter(*args, **kwargs)
        self.add(element)
        return element

    def add_top_image(self, *args, **kwargs):
        element = CardImageTop(*args, **kwargs)
        self.add(element)
        return element

    def add_bottom_image(self, *args, **kwargs):
        element = CardImageBottom(*args, **kwargs)
        self.add(element)
        return element

class CardHeader(BootstrapElement):
    TAG = "div"
    CLASS = "card-header"

class CardBody(BootstrapElement):
    TAG = "div"
    CLASS = "card-body"

    def __init__(self, *args, title=None, subtitle=None, text=None, **kwargs):
        super().__init__(*args, **kwargs)

        if title:
            self.add_title(title)
        if subtitle:
            self.add_subtitle(subtitle)
        if text:
            self.add_text(text)

    def add_title(self, content):
        element = CardTitle(content)
        self.add(element)
        return element

    def add_subtitle(self, content):
        element = CardSubtitle(content)
        self.add(element)
        return element

    def add_text(self, content):
        element = CardText(content)
        self.add(element)
        return element

    def add_link(self, title, href):
        element = CardLink(title, href=href)
        self.add(element)
        return element

class CardTitle(BootstrapElement):
    TAG = "h5"
    CLASS = "card-title"

class CardSubtitle(BootstrapElement):
    TAG = "h6"
    CLASS = "card-subtitle text-muted"

class CardText(BootstrapElement):
    TAG = "p"
    CLASS = "card-text"

class CardLink(BootstrapElement):
    TAG = "a"
    CLASS = "card-link"

class CardFooter(BootstrapElement):
    TAG = "div"
    CLASS = "card-footer"

class ImageElement(BootstrapElement):
    TAG = "img"
    KIND = "void"

    def __init__(self, src, *args, **kwargs):
        super().__init__(*args, src=src, **kwargs)

class CardImageTop(ImageElement):
    CLASS = "card-img-top"

class CardImageBottom(ImageElement):
    CLASS = "card-img-bottom"

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
