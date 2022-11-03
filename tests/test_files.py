import yaml
from pathlib import Path
import pytest

def read_test_files():
    tests = []
    p = Path(__file__).parent
    files = p.rglob('*.yml')
    for f in files:
        tests.extend(list(yaml.safe_load_all(f.open())))
    return tests

# Get all tests
testdata = read_test_files()
test_ids = [t['name'] for t in testdata]

@pytest.mark.parametrize('testspec', testdata, ids=test_ids)
def test_code(testspec):
    code = testspec['code']
    expected_html = testspec['html']

    from patterns import html
    env = {"html": html}
    element = eval(code, env)
    html = element.render()

    assert html.strip() == expected_html.strip()