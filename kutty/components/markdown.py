"""The kutty Markdown component.

Usage:

````python
element = Markdown("\
# A markdown component

You can use **bold**, *italic*, and `code` inside.

```
The fenced code extension is also enabled.
```
")
````

You can also use the `add_markdown()` method.

```python
element = Markdown()
element.add_markdown("*some markdown text*\n**bold**")
```

You can pass an "extensions" keyword argument while initialising
Markdown to add custom extensions. By default, only the `fenced_code`
extension is enabled.
"""

import markdown

from kutty import html


class Markdown(html.HTMLElement):
    TAG = "div"

    def __init__(self, text=None, extensions=("fenced_code",), **kwargs):
        super().__init__(**kwargs)
        self.extensions = extensions
        if text:
            self.add_markdown(text)

    def add_markdown(self, text):
        rendered_html = html.HTML(markdown.markdown(text, extensions=self.extensions))
        self.add(rendered_html)
        return rendered_html
