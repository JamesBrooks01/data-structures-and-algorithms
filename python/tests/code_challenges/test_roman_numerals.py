import pytest
from code_challenges.roman_numerals import roman_counter


def test_4():
  actual = roman_counter("IV")
  expected = 4
  assert actual == expected

def test_1984():
  actual = roman_counter("MCMLXXXIV")
  expected = 1984
  assert actual == expected

def test_2021():
  actual = roman_counter("MMXXI")
  expected = 2021
  assert actual == expected

def test_1974():
  actual = roman_counter("MCMLXXIV")
  expected = 1974
  assert actual == expected

def test_1900():
  actual = roman_counter("MCM")
  expected = 1900
  assert actual == expected

def test_142():
  actual = roman_counter("CXLII")
  expected = 142
  assert actual == expected
