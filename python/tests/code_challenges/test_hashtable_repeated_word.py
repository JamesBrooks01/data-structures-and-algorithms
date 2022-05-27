import pytest
from code_challenges.hashtable_repeated_word import first_repeated_words


# @pytest.mark.skip("TODO")
def test_blank():
    actual = first_repeated_words("")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_no_repeat():
    actual = first_repeated_words("nobody here but us chickens")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_a():
    actual = first_repeated_words("apple apple")
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_b_a():
    actual = first_repeated_words("apple banana apple")
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_b_a_b():
    actual = first_repeated_words("apple banana apple banana")
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_b_b_a():
    actual = first_repeated_words("apple banana banana apple")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_ignore_case():
    actual = first_repeated_words("apple banana BANANA apple")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_ignore_case_flipped():
    actual = first_repeated_words("apple BANANA banana apple")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_punctuation():
    actual = first_repeated_words("apple? BANANA! banana, apple.")
    expected = "banana"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_punctuation_joins():
    txt = """
  apple
  apple.apple-apple
  banana
  apple?apple
  banana
  """

    actual = first_repeated_words(txt)
    expected = "banana"
    assert actual == expected
