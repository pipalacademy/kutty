import argparse
import sys
from .app import app

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("path", help="Path to pages to serve")
    return p.parse_args()

def main():
    args = parse_args()
    sys.path.append(args.path)
    app.path = args.path
    app.init_app()
    print("layout", id(app), app.title, app.layout.__class__)
    app.run()

if __name__ == "__main__":
    main()