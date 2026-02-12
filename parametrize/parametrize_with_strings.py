import pytest


"""
This is a test case for checking the length of a string.
Good for testing text inputs.
"""
@pytest.mark.parametrize("name",["anil","chaudhary","python"])
def test_name_length(name):
    assert len(name) > 0
    assert len(name) < 10