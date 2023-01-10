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

## Empty Condition

The empty condition used for Optional is whether or not `element.children`
is an empty list.

This doesn't generalise well for few cases:
    - For a void element, where there is supposed to be no closing tag.
    For example an <img> element or a <hr> or <br>.
    - For empty elements that are there to provide visual effect (such
    as extra padding between two other elements).
    - For nested optionals where self.children can itself have Optionals
"""
from kutty import html


class Optional(html.Element):
    def __init__(self, e):
        self.e = e

    def __getattr__(self, attr):
        # pass through
        return getattr(self.e, attr)

    def render(self):
        if self.e.children:
            return self.e.render()
        else:
            return ""
