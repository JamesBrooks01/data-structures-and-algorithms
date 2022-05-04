import pytest
from code_challenges.stack_queue_brackets import multi_bracket_validation


# @pytest.mark.skip("TODO")
def test_validates_two_square_brackets():
    actual = multi_bracket_validation("[]")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_fails_two_square_brackets_flipped():
    actual = multi_bracket_validation("][")
    expected = False
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_validates_two_braces():
    actual = multi_bracket_validation("{}")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_fails_two_braces_flipped():
    actual = multi_bracket_validation("}{")
    expected = False
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_validates_two_parentheses():
    actual = multi_bracket_validation("()")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_fails_two_parentheses_flipped():
    actual = multi_bracket_validation(")(")
    expected = False
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_multi():
    actual = multi_bracket_validation("{}(){}")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_nested():
    actual = multi_bracket_validation("{([])}")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_mismatched():
    actual = multi_bracket_validation("[}")
    expected = False
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_multi_backwards_brackets():
    actual = multi_bracket_validation("}(){")
    expected = False
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_multi_backwards_brackets_ordered():
    actual = multi_bracket_validation("}{()")
    expected = False
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_multi_backwards_brackets_ordered_correct_first():
    actual = multi_bracket_validation("()}{")
    expected = False
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_multi_backwards_brackets_ordered_correct_first():
    actual = multi_bracket_validation("(}{)")
    expected = False
    assert actual == expected

@pytest.mark.parametrize(
    "input, expected",
    [
        ('{}', True),
        ('{}(){}', True),
        ("()[[Extra Characters]]", True),
        ("(){}[[]]", True),
        ("{}{Code}[Fellows](())", True),
        ("[({}]", False),
        ("(](", False),
        ("{(})", False)
    ],
)

# @pytest.mark.skip("TODO")
def test_examples(input, expected):
    actual = multi_bracket_validation(input)
    assert actual == expected
