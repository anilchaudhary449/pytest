import pytest

"""
This is a test case for checking the even numbers.
Good for testing conditional expected results.

Checks if a number is even against expected boolean.
"""

@pytest.mark.parametrize("num,is_even",[
    (2, True),
    (3,False),
    (5,False),
    (7,False),
    (8,True),
    (9,False),
    (10,True)
])

def test_is_even(num,is_even):
    assert (num%2==0) == is_even