import pytest


"""
Perfect for testing structured data like dicts or JSON
"""
test_data = [
    {
        "input_data":[1,2,3],"expected_sum":6
    },
    {
        "input_data":[4,5,6],"expected_sum":15
    },
    {
        "input_data":[7,8,9],"expected_sum":24
    },
    {
        "input_data":[10,11,12],"expected_sum":33
    },
    {
        "input_data":[13,14,15],"expected_sum":42
    }
]

@pytest.mark.parametrize("test_case",test_data)
def test_sum(test_case):
    assert sum(test_case["input_data"]) == test_case["expected_sum"]