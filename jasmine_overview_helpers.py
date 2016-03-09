import re

KEYWORD_RE = r'(describe|it)\s*\('
KEYWORD_WITH_BEFORE_AFTER_RE = r'(describe|beforeEach|afterEach|it)\s*\('


def get_name(code):
    # Remove function defs
    name = re.sub(
        r'[\s,]*function[^"\']*$',
        '',
        code
    )

    # Make the formatting nicer
    if name[-1] == '(':
        name = name[:-1]
    else:
        name = re.sub(
            r'\s*\(\s*',
            ': ',
            name
        )
    name = name.rstrip()

    return name
