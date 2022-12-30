"""Kutty web app.
"""

from re import A
from flask import Flask, abort
from pathlib import Path
from . import Layout

class Kutty(Flask):
    def __init__(self, path, title="Kutty"):
        super().__init__(__name__)
        self.path = path
        self.title = title
        self.layout = self.get_layout()

        self.route("/")(self.render_path)
        self.route("/<path:path>")(self.render_path)

    def get_layout(self):
        path = self.get_path("_layout.py")
        if path.exists():
            layout = self.exec_path(path, "layout")
        else:
            layout = Layout(self.title)
        return layout

    def get_path(self, filename, suffix=None):
        if suffix:
            filename = filename + suffix
        return Path(self.path) / filename

    def exec_path(self, path, target_var):
        code = path.read_text()
        env = {}
        exec(code, env)
        return env[target_var]

    def render_path(self, path=""):
        if path == "" or path.endswith("/"):
            path += "index"

        py_path = self.get_path(path, suffix=".py")
        if not py_path.exists():
            return abort(404)

        page = self.exec_path(py_path, 'page')
        return self.layout.render_page(page)

def parse_args():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("path", help="Path to pages to serve")
    return p.parse_args()

def main():
    import sys
    args = parse_args()
    sys.path.append(args.path)
    app = Kutty(args.path)
    app.run()

if __name__ == "__main__":
    main()