import pytest
from code_challenges.merge_sort import merge_sort

def test_list_one():
  list = [8,4,23,42,16,15]
  actual = merge_sort(list)
  expected = [4,8,15,16,23,42]
  assert actual == expected

def test_list_reverse():
  list = [20,18,12,8,5,-2]
  actual = merge_sort(list)
  expected = [-2,5,8,12,18,20]
  assert actual == expected

def test_list_uniques():
  list = [5,12,7,5,5,7]
  actual = merge_sort(list)
  expected = [5,5,5,7,7,12]
  assert actual == expected

def test_list_near_sorted():
  list = [2,3,5,7,13,11]
  actual = merge_sort(list)
  expected = [2,3,5,7,11,13]
  assert actual == expected
