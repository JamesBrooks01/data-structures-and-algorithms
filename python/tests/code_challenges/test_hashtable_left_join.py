import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NONE"],
        ["wrath", "anger", "delight"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

# @pytest.mark.skip("TODO")
def test_custom_one():
    synonyms = {
        "meditative": "cognative",
        "motorcade": "caravan",
        "concurrent": "synchronous",
        "surround": "encircle",
        "agreeable": "copacetic",
    }
    antonyms = {
        "meditative": "unreflective",
        "agreeable": "disagreeable",
        "destroy": "construct",
        "apex": "nadir",
        "declination": "ascent",
    }

    expected = [
        ['meditative', 'cognative', 'unreflective'],
        ['motorcade', 'caravan', 'NONE'],
        ['concurrent', 'synchronous', 'NONE'],
        ['surround', 'encircle', 'NONE'],
        ['agreeable', 'copacetic', 'disagreeable']
        ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

# @pytest.mark.skip("TODO")
def test_custom_two():
    left = {
        "1": "2",
        "3": "4",
        "5": "6",
        "7": "8",
        "9": "10",
    }
    right = {
        "1": "word1",
        "7": "word2",
        "9": "word3",
        "15": "word4",
        "21": "word5",
    }

    expected = [
    ['1', '2', 'word1'],
    ['3', '4', 'NONE'],
    ['5', '6', 'NONE'],
    ['7', '8', 'word2'],
    ['9', '10', 'word3']
    ]

    actual = left_join(left, right)

    assert actual == expected
