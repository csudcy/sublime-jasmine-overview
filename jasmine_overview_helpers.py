import re

KEYWORD_RE = r'(describe|it)\w*\('
KEYWORD_WITH_BEFORE_AFTER_RE = r'(describe|beforeEach|afterEach|it)\w*\('


def get_name(code):
    # Remove function defs
    name = re.sub(
        r',?\s*function\s*\(\s*\)\s*{?',
        '',
        code
    )

    # Make the formatting nicer
    name = name.rstrip()
    if name[-1] == '(':
        name = name[:-1]
    else:
        name = name.replace('(', ': ')

    return name
