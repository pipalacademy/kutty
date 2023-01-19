"""The Code component.

Renders the code as a pre element applies syntax highlighting using Pygments.

Sample Usage:

```
from kutty import Page, Code

code = '''
print("hello, world1")
'''

page = Page("Code demo")
page << Code(code)
```
"""
from .. import html
from pygments import highlight
from pygments.lexers import guess_lexer, get_lexer_by_name
from pygments.formatters import HtmlFormatter

def Code(code, lang=None):
    if lang is None:
        lexer = guess_lexer(code)
    else:
        lexer = get_lexer_by_name(lang)

    _html = highlight(code, lexer, HtmlFormatter())
    return html.HTML(_html)