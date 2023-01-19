import glob
import yaml
from flask import Flask

from kutty import html, Code
from kutty.bootstrap import *
from kutty.bootstrap.layout import Layout, Page

app = Flask(__name__)
layout = Layout("Bootstrap Preview")
layout.add_stylesheet("https://pygments.org/_static/pygments.css")

style = """
<style type="text/css">
.highlight {
    padding: 20px;
}
.highlight pre {
    margin: 0;
    line-height: inherit;
}
</style>
"""

@app.route("/")
def index():
    page = Page("")
    page << html.HTML(style)

    for file_path in glob.glob("tests/bootstrap/test_*.yml"):
        section = Section(title=get_title_from_file_path(file_path))
        with open(file_path) as f:
            for test_case in yaml.safe_load_all(f):
                name, code = test_case["name"], test_case["code"]
                section << Preview(name=name, code=code)

        page << section

    return layout.render_page(page)


def get_title_from_file_path(file_path):
    return file_path.rsplit("/", 1)[-1].split(".", 1)[0][5:].replace("_", " ").title()


class Section(html.HTMLElement):
    TAG = "div"
    CLASS = "mb-5 border-bottom"

    def __init__(self, *args, title=None, **kwargs):
        super().__init__(*args, **kwargs)

        if title is not None:
            self.add(html.h1(title))


class Preview(html.HTMLElement):
    TAG = "div"
    CLASS = "card mb-4"

    def __init__(self, *args, name, code, **kwargs):
        super().__init__(*args, **kwargs)

        env = get_exec_env()
        exec(code, env)
        result = env["result"]

        self.add(
            html.div(name.title(), class_="card-header")
        )
        self.add(
            html.div(class_="card-body").add(
                html.div(result),
            )
        )
        self.add(Code(code))

def get_exec_env():
    env = {}
    exec("from kutty import *", env)
    return env
