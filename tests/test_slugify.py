from slugify import slugify


def test_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_extra_whitespace():
    assert slugify("  Multiple   spaces here  ") == "multiple-spaces-here"


def test_numbers_are_kept():
    assert slugify("Item 42 in stock") == "item-42-in-stock"


def test_leading_and_trailing_punctuation_stripped():
    assert slugify("--Already-a-slug--") == "already-a-slug"


def test_empty_string():
    assert slugify("") == ""
