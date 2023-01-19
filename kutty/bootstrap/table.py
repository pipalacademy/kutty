"""The Bootstrap Table component.

Sample usage:

```python
from kutty.bootstrap import Table

table = Table(columns=["First name", "Last name", "Handle"])
table.add_row(["Foo", "Bar", "@baz"])
table.add_row(["Spam", "Ham", "@eggs"])
```

Each row can also be constructed by adding one cell at a time:

```python
from kutty.bootstrap import Table

table = Table(columns=["First name", "Last name", "Handle"])
for user in users:
    row = table.add_row()
    row.add_cell(user.first)
    row.add_cell(user.last)
    row.add_cell(user.handle)
```

Tables can also be constructed by hand, but you need to add
the Table Head and Table Body separately.

```python
from kutty.bootstrap.table import Table, TableHead, TableBody, TableRow, TableCell

table = Table(
    TableHead(
        TableRow(
            TableCell("First Name", header=True, scope="col"),
            TableCell("Last Name", header=True, scope="col"),
            TableCell("Handle", header=True, scope="col")
        ),
    ),
    TableBody(
        TableRow(
            TableCell("Foo"), TableCell("Bar"), TableCell("@baz"),
        ),
        TableRow(
            TableCell("Spam"), TableCell("Ham"), TableCell("@eggs")
        )
    )
)
```

You can also access the default Table Head and Table Body with `table.head`
and `table.body`. These will be of types `TableHead` and `TableBody`
respectively.
"""

from .base import BootstrapElement
from kutty import Optional


class Table(BootstrapElement):
    TAG = "table"
    CLASS = "table"

    def __init__(self, *args, columns=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.head = Optional(TableHead())
        self.body = Optional(TableBody())

        self.add(self.head, self.body)

        if columns:
            self.head.add_row(columns)

    def add_row(self, elements=None):
        """See TableBody.add_row.
        """
        return self.body.add_row(elements)


class TableHead(BootstrapElement):
    TAG = "thead"

    def add_row(self, elements=None):
        """Takes a list as argument and adds a row with those elements
        inside a table header (th) cell.

        Sets scope="col" attribute for the cell.

        Simply returns an empty row if no argument is given.

        Returns a handle to the added row.
        """
        row = TableRow()
        self.add(row)
        for element in (elements or []):
            row.add_cell(element, header=True, scope="col")
        return row


class TableBody(BootstrapElement):
    TAG = "tbody"

    def add_row(self, elements=None):
        """Takes a list as argument and adds a row with those elements
        inside a table data (td) cell.

        Simply returns an empty row if no argument is given.

        Returns a handle to the added row.
        """
        row = TableRow()
        self.add(row)
        for element in (elements or []):
            row.add_cell(element)
        return row


class TableRow(BootstrapElement):
    TAG = "tr"

    def add_cell(self, *args, **kwargs):
        cell = TableCell(*args, **kwargs)
        self.add(cell)
        return cell


class TableCell(BootstrapElement):
    def __init__(self, *args, header=False, **kwargs):
        self.TAG = "th" if header else "td"
        super().__init__(*args, **kwargs)
