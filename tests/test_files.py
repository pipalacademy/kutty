import re
import yaml
from pathlib import Path
import pytest

def read_test_files():
    tests = []
    p = Path(__file__).parent
    files = p.rglob('**/*.yml')
    for f in files:
        tests.extend(list(yaml.safe_load_all(f.open())))
    return tests

# Get all tests
testdata = read_test_files()
test_ids = [t['name'] for t in testdata]

@pytest.mark.parametrize('testspec', testdata, ids=test_ids)
def test_code(testspec):
    code = testspec['code'].strip()
    expected_html = testspec['html']

    from patterns import html
    env = {}
    exec("from patterns import *", env)
    if code.count("\n") > 0:
        exec(code, env)
        html = env["html"]
    else:
        element = eval(code, env)
        html = element.render()

    assert html.strip() == despace(expected_html.strip())

re_newline = re.compile(r"\n *", re.M)

def despace(text):
    return re_newline.sub("", text)
