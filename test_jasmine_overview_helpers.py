import re

import pytest

import jasmine_overview_helpers


@pytest.mark.parametrize(
    'code',
    (
        # No spaces
        'describe("A description",function(){',
        'xdescribe("A description",function(){',
        'it("A description",function(){',
        'xit("A description",function(){',

        # Lots of spaces
        '    describe( "A description" , function ( )  { ',
        '    xdescribe( "A description" , function ( )  { ',
        '    it( "A description" , function ( ) { ',
        '    xit( "A description" , function ( ) { ',
    )
)
def test_keyword_re_matches(code):
    assert re.search(jasmine_overview_helpers.KEYWORD_RE, code) is not None


@pytest.mark.parametrize(
    'code',
    (
        # No spaces
        'describe("A description",function(){',
        'xdescribe("A description",function(){',
        'it("A description",function(){',
        'xit("A description",function(){',
        'beforeEach(function(){',
        'afterEach(function(){',

        # Lots of spaces
        '    describe ( "A description" , function ( )  { ',
        '    xdescribe ( "A description" , function ( )  { ',
        '    it ( "A description" , function ( ) { ',
        '    xit ( "A description" , function ( ) { ',
        '    beforeEach ( function ( )  { ',
        '    afterEach ( function ( )  { ',
    )
)
def test_keyword_with_before_after_re_matches(code):
    assert re.search(jasmine_overview_helpers.KEYWORD_WITH_BEFORE_AFTER_RE, code) is not None


@pytest.mark.parametrize(
    'code',
    (
        'beforeEach(function() {',
        'afterEach(function() {',
        'this.find_stub.withArgs("textarea.comment").returns({val: this.val_stub});',
        'this.view.init(this.my_campaign);',
        'Just a sentence with the word describe in',
        'Just a sentence with the word it in',
        'Just a sentence with the word xdescribe in',
        'Just a sentence with the word xit in',
    )
)
def test_keyword_re_does_not_match(code):
    assert re.search(jasmine_overview_helpers.KEYWORD_RE, code) is None


@pytest.mark.parametrize(
    'code',
    (
        'this.find_stub.withArgs("textarea.comment").returns({val: this.val_stub});',
        'this.view.init(this.my_campaign);',
        'Just a sentence with the word describe in',
        'Just a sentence with the word it in',
        'Just a sentence with the word xdescribe in',
        'Just a sentence with the word xit in',
        'Just a sentence with the word beforeEach in',
        'Just a sentence with the word afterEach in',
    )
)
def test_keyword_with_before_after_re_does_not_match(code):
    assert re.search(jasmine_overview_helpers.KEYWORD_WITH_BEFORE_AFTER_RE, code) is None


@pytest.mark.parametrize(
    'code,expected_name',
    (
        # No spaces
        (
            'describe("A description",function(){',
            'describe: "A description"'
        ),
        (
            'xdescribe("A description",function(){',
            'xdescribe: "A description"',
        ),
        (
            'it("A description",function(){',
            'it: "A description"',
        ),
        (
            'xit("A description",function(){',
            'xit: "A description"',
        ),
        (
            'beforeEach(function(){',
            'beforeEach',
        ),
        (
            'afterEach(function(){',
            'afterEach',
        ),

        # Lots of spaces
        (
            '    describe ( "A description" , function ( )  { ',
            '    describe: "A description"',
        ),
        (
            '    xdescribe ( "A description" , function ( )  { ',
            '    xdescribe: "A description"',
        ),
        (
            '    it ( "A description" , function ( ) { ',
            '    it: "A description"',
        ),
        (
            '    xit ( "A description" , function ( ) { ',
            '    xit: "A description"',
        ),
        (
            '    beforeEach ( function ( )  { ',
            '    beforeEach',
        ),
        (
            '    afterEach ( function ( )  { ',
            '    afterEach',
        ),

        # Lots of spaces with comments
        (
            '    describe ( "A description" , function ( )  { # Commenty McComment',
            '    describe: "A description"',
        ),
        (
            '    xdescribe ( "A description" , function ( )  { # Commenty McComment',
            '    xdescribe: "A description"',
        ),
        (
            '    it ( "A description" , function ( ) { # Commenty McComment',
            '    it: "A description"',
        ),
        (
            '    xit ( "A description" , function ( ) { # Commenty McComment',
            '    xit: "A description"',
        ),
        (
            '    beforeEach ( function ( )  { # Commenty McComment',
            '    beforeEach',
        ),
        (
            '    afterEach ( function ( )  { # Commenty McComment',
            '    afterEach',
        ),
    )
)
def test_get_name_extracts_correct_name(code, expected_name):
    name = jasmine_overview_helpers.get_name(code)
    assert name == expected_name
