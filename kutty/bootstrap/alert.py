"""The Alert component.

Sample usage:

```
from kutty.bootstrap import Alert

alert = Alert(dismissible=True)
alert.add("Congrats! You've passed the test.")
```

With links:

```
from kutty import Link
from kutty.bootstrap import Alert

alert = Alert(dismissible=False)
alert.add([
    "A simple primary alert with ",
    Link("an example link", href="/link"),
    ". Give it a click if you like."
])
```

With heading:

```
from kutty import Link
from kutty.bootstrap import Alert

alert = Alert()
alert.add_heading("Well done")
alert.add("You have solved the assignment successfully.")
```
"""
from kutty import Link, html
from .base import BootstrapElement


class Alert(BootstrapElement):
    def __init__(self, dismissible=True):
        self._dismissible = dismissible
        self.content = []

    @property
    def dismissible(self):
        # read-only
        return self._dismissible

    def add(self, element):
        # TODO: This needs to be there, but needs changing in HTMLElement
        # if isinstance(element, Link):
        #     element.add_class("alert-link")
        return self.content.append(element)

    def add_heading(self, content):
        return self.add(
            html.h4(class_="alert-heading").add(content)
        )

    def render(self):
        classes = ["alert"]
        if self.dismissible:
            classes += self.get_dismissible_classes()

        node = html.div(class_=" ".join(classes), role="alert")
        for element in self.content:
            node << element

        if self.dismissible:
            node << self.get_dismiss_button()

        return node.render()

    def get_dismissible_classes(self):
        return ["alert-dismissible", "fade", "show"]

    def get_dismiss_button(self):
        button = html.button(type="button", class_="close")
        button.attrs["data-dismiss"] = "alert"

        button << html.span("&times;")
        return button
