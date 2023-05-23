from .. import html


class Navbar(html.HTMLElement):
    TAG = "nav"
    CLASS = "navbar navbar-expand-lg navbar-light bg-light"

    def __init__(self, title):
        super().__init__()
        self.container = html.div(class_="container")

        self.branding = html.a(title, class_="navbar-brand", href="/")

        self.left_entries = html.ul(class_="navbar-nav mr-auto")
        self.right_entries = html.ul(class_="navbar-nav")

        navbar_content_id = "navbar-content"
        self.content = html.div(
            class_="collapse navbar-collapse justify-content-between",
            id=navbar_content_id
        ).add(
            self.left_entries, self.right_entries,
        )

        self << self.container

        self.container << self.branding
        self.container << NavbarToggler(target=f"#{navbar_content_id}")
        self.container << self.content

    def add_link(self, element, url, right=False):
        entry = NavEntry(element, url)
        if right:
            self.right_entries << entry
        else:
            self.left_entries << entry
        return entry


class NavEntry(html.HTMLElement):
    TAG = "li"
    CLASS = "nav-item"

    def __init__(self, element, url):
        super().__init__()
        self << html.a(class_="nav-link", href=url).add(element)


class NavbarToggler(html.HTMLElement):
    TAG = "button"
    CLASS = "navbar-toggler"

    def __init__(self, *args, target, **kwargs):
        super().__init__(
                *args,
                type="button",
                data_bs_toggle="collapse",
                data_bs_target=target,
                **kwargs)
        self << html.span(class_="navbar-toggler-icon")
