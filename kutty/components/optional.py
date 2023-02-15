"""The Optional component.

Optional component can be used to wrap another element, such that it
will only render something meaningful when it has some content.

Example usage:

```python
from kutty import Optional, html

d = html.div(
    Optional(html.div())
    Optional(html.div("foo"))
)

print(d.render())
```

This will output:
```html
<div>
    <div>foo</div>
</div>
```

Notice that there is only one child div element, which has some content.

## Render Condition

`Optional`'s constructor takes a second argument as the render condition.
This is a function that takes the element and returns a boolean telling
if the element should be rendered.

The default for this render condition is `is_not_empty` which will render
the element if its `.is_empty()` method returns a Falsey value.
"""

from kutty import html


def is_base_element(element):
    return (isinstance(element, html.Text) or
            isinstance(element, html.HTML))

def is_not_empty(element):
    return not element.is_empty()

class Optional(html.Element):
    def __init__(self, e, render_condition=is_not_empty):
        self.e = e
        self.render_condition = render_condition

    def __getattr__(self, attr):
        # pass through
        return getattr(self.e, attr)

    def render(self):
        if self.render_condition(self.e):
            return self.e.render()
        else:
            return ""

    def add(self, *args, **kwargs):
        return self.e.add(*args, **kwargs)

    def is_empty(self):
        return self.e.is_empty()
