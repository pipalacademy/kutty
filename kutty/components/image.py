"""The Image component.

Sample usage:

```
from kutty import Image
img = Image("https://via.placeholder.com/150", alt="placeholder image")
print(img)
```
"""

from .. import html

def Image(src, *args, **kwargs):
    return html.img(*args, src=src, **kwargs)
