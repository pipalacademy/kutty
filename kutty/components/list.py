"""The List component.

Sample Usage:

```
from kutty import List
numbers = List(["one", "two", "three"])
print(numbers)
```

The above example would produce:

```
<ul>
    <li>one</li>
    <li>two</li>
    <li>three</li>
</ul>
```

The same example could also be written as:

```
from kutty import List
numbers = List()
numbers << 'one'
numbers << 'two'
numbers << 'three'
print(numbers)
```

"""
from .. import html

class List(html.Element):
    def __init__(self, elements=None):
        self.elements = list(elements or [])

    def add(self, element):
        """Adds a new row to the table and returns the TableRow object.
        """
        self.elements.add(element)
        return self

    def render(self):
        node = html.ul()
        for e in self.elements:
            node << html.li(e)
        return node.render()
