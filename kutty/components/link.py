"""The Link component.

Sample Usage:

```
from kutty import Link
a = Link("Google", href="https://google.com")
print(a)
```
"""
from .. import html

def Link(content, **kwargs):
    a = html.a(**kwargs)
    a << content
    return a