import pytest
from code_challenges.stack_queue_pseudo import PseudoQueue


def test_exists():
    assert PseudoQueue


# @pytest.mark.skip("TODO")
def test_enqueue_one():
    pq = PseudoQueue()
    pq.enqueue("apples")
    actual = pq.dequeue()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_enqueue_two():
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")

    actual = pq.dequeue()
    expected = "apples"
    assert actual == expected

    actual = pq.dequeue()
    expected = "bananas"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_enqueue_dequeue_enqueue_dequeue():
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")

    pq.dequeue()

    pq.enqueue("cucumbers")
    pq.enqueue("dates")

    actual = [pq.dequeue(), pq.dequeue(), pq.dequeue()]

    expected = ["bananas", "cucumbers", "dates"]

    assert actual == expected

def test_pseudo_queue_was_it_that_easy():
    pq = PseudoQueue()
    pq.enqueue("1")
    pq.enqueue("2")
    pq.enqueue("3")
    result_1 = pq.dequeue()
    pq.dequeue()
    pq.enqueue("4")
    pq.enqueue("5")
    pq.enqueue("6")
    pq.dequeue()
    result_2 = pq.dequeue()

    expected_1 = "1"
    expected_2 = "4"

    assert result_1 == expected_1
    assert result_2 == expected_2

def test_pseudo_queue_was_it_that_easy_2():
    pq = PseudoQueue()
    pq.enqueue("1")
    pq.enqueue("2")
    pq.enqueue("3")
    result_1 = pq.dequeue()
    pq.enqueue("4")
    pq.enqueue("5")
    pq.enqueue("6")
    result_2 = pq.dequeue()

    expected_1 = "1"
    expected_2 = "2"

    assert result_1 == expected_1
    assert result_2 == expected_2

def test_pseudo_queue_was_it_that_easy_3():
    pq = PseudoQueue()
    pq.enqueue("1")
    pq.enqueue("2")
    pq.enqueue("3")
    result_1 = pq.dequeue()
    pq.dequeue()
    pq.dequeue()
    pq.enqueue("4")
    pq.enqueue("5")
    pq.enqueue("6")
    pq.dequeue()
    result_2 = pq.dequeue()

    expected_1 = "1"
    expected_2 = "5"

    assert result_1 == expected_1
    assert result_2 == expected_2

def test_pseudo_queue_was_it_that_easy_4():
    pq = PseudoQueue()
    pq.enqueue("1")
    pq.enqueue("2")
    pq.enqueue("3")
    result_1 = pq.dequeue()
    pq.dequeue()
    pq.dequeue()
    pq.enqueue("4")
    pq.enqueue("5")
    pq.enqueue("6")
    pq.dequeue()
    pq.dequeue()
    result_2 = pq.dequeue()

    expected_1 = "1"
    expected_2 = "6"

    assert result_1 == expected_1
    assert result_2 == expected_2

def test_pseudo_queue_was_it_that_easy_5():
    pq = PseudoQueue()
    pq.enqueue("1")
    pq.enqueue("2")
    pq.enqueue("3")
    pq.dequeue()
    result_1 = pq.dequeue()
    pq.dequeue()
    pq.enqueue("4")
    pq.enqueue("5")
    pq.enqueue("6")
    pq.dequeue()
    pq.dequeue()
    result_2 = pq.dequeue()

    expected_1 = "2"
    expected_2 = "6"

    assert result_1 == expected_1
    assert result_2 == expected_2
