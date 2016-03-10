import re

def make_re(*keywords):
    return r'^\s*(' + '|'.join(keywords) + r')\s*\('

KEYWORD_RE = make_re('describe', 'xdescribe', 'it', 'xit')
KEYWORD_WITH_BEFORE_AFTER_RE = make_re('describe', 'xdescribe', 'it', 'xit', 'beforeEach', 'afterEach')


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
