import re

import pytest

import jasmine_overview_helpers


@pytest.mark.parametrize(
    'code',
    (
        'describe("A suite", function() {',
        'xdescribe("A spec", function() {',
        '  it("contains spec with an expectation", function() {',
        '  xit("can be declared \'xit\'", function() {',
    )
)
def test_keyword_re_matches(code):
    assert re.match(jasmine_overview_helpers.KEYWORD_RE, code) is not None
