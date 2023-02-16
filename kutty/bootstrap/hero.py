"""The Bootstrap Hero component

Usage:

```python
from kutty.bootstrap import Hero

hero = Hero(
    title="Hello, world!",
    subtitle="This is a simple hero unit",
    text="Hello world is a nice placeholder",
)
hero.add_cta("Learn More", href="/more")
print(hero.render())
```
"""

from kutty import Optional

from .base import BootstrapElement


class Hero(BootstrapElement):
    TAG = "div"
    CLASS = "jumbotron"

    def __init__(
            self,
            *args,
            title=None, subtitle=None, text=None,
            **kwargs):
        super().__init__(*args, **kwargs)

        self.header = Optional(HeroHeader())
        self.body = Optional(HeroBody())
        separator = Optional(
            HeroSeparator(),
            render_condition=lambda _: (not self.header.is_empty() and
                                        not self.body.is_empty()))

        self.container = Optional(HeroContainer())
        self.container << self.header
        self.container << separator
        self.container << self.body

        self << self.container

        if title:
            self.add_title(title)
        if subtitle:
            self.add_subtitle(subtitle)
        if text:
            self.add_text(text)

    def add_title(self, *args, **kwargs):
        return self.header.add_title(*args, **kwargs)

    def add_subtitle(self, *args, **kwargs):
        return self.header.add_subtitle(*args, **kwargs)

    def add_text(self, *args, **kwargs):
        return self.body.add_text(*args, **kwargs)

    def add_cta(self, *args, **kwargs):
        return self.body.add_cta(*args, **kwargs)


class HeroContainer(BootstrapElement):
    TAG = "div"
    CLASS = "container"

    def is_empty(self):
        return all(c.is_empty()
                   if isinstance(c, HeroHeader) or isinstance(c, HeroBody)
                   else False
                   for c in self.children)


class HeroHeader(BootstrapElement):
    TAG = "div"

    def add_title(self, title):
        title = HeroTitle(title)
        self << title
        return title

    def add_subtitle(self, subtitle):
        subtitle = HeroSubtitle(subtitle)
        self << subtitle
        return subtitle


class HeroBody(BootstrapElement):
    TAG = "div"

    def add_text(self, text):
        element = HeroText(text)
        self << element
        return element

    def add_cta(self, text, href):
        cta = HeroCTA(text=text, href=href)
        self << cta
        return cta


class HeroSeparator(BootstrapElement):
    TAG = "hr"
    KIND = "void"
    CLASS = "my-4"


class HeroTitle(BootstrapElement):
    TAG = "h1"
    CLASS = "display-4"


class HeroSubtitle(BootstrapElement):
    TAG = "p"
    CLASS = "lead"


class HeroText(BootstrapElement):
    TAG = "p"


class HeroCTA(BootstrapElement):
    TAG = "a"
    CLASS = "btn btn-primary btn-lg"

    def __init__(self, *args, text, **kwargs):
        super().__init__(*args, **kwargs)
        self.add(text)
