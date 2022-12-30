"""Kutty web app.
"""

from flask import Flask, abort
from pathlib import Path
from .layout import Layout, RawPage

class Kutty(Flask):
    def __init__(self, path, title="Kutty"):
        super().__init__(__name__)
        self.path = path
        self.title = title
        self.layout = Layout(self.title)

        self.route("/")(self.render_path)
        self.route("/<path:path>")(self.render_path)

    def init_app(self):
        """Initialize the app using _app.py
        """
        path = self.get_path("_app.py")
        if path.exists():
            self.exec_path(path)

    def get_path(self, filename, suffix=None):
        if suffix:
            filename = filename + suffix
        return Path(self.path) / filename

    def exec_path(self, path, target_var=None):
        env = {}
        exec(_compile_file(path), env)
        if target_var:
            return env[target_var]

    def render_path(self, path=""):
        if path == "" or path.endswith("/"):
            path += "index"

        py_path = self.get_path(path, suffix=".py")
        if not py_path.exists():
            return abort(404)

        page = self.exec_path(py_path, 'page')

        if isinstance(page, RawPage):
            return page.make_response()
        else:
            return self.layout.render_page(page)

app = Kutty(".")

cache = {}
def _compile_file(path):
    if path not in cache:
        cache[path] = compile(path.read_text(), str(path), "exec")
    return cache[path]

