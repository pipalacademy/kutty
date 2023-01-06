"""The Image component.

Sample usage:

```
from kutty import Image
img = Image("https://via.placeholder.com/150", alt="placeholder image")
print(img)
```
"""

from .. import html

def Image(src, **kwargs):
    return html.img(src, **kwargs)
