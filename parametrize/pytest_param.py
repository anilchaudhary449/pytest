import pytest

"""
'id' is used to name each test case.
Useful for readable test reports.
"""


@pytest.mark.parametrize("num,expected",[
    pytest.param(1, True, id="1_is_odd"),
    pytest.param(2, False, id="2_is_even"),
    pytest.param(3, True, id="3_is_odd"),
    pytest.param(4, False, id="4_is_even"),
    pytest.param(5, True, id="5_is_odd"),
    pytest.param(6, False, id="6_is_even"),
    pytest.param(7, True, id="7_is_odd"),
    pytest.param(8, False, id="8_is_even"),
    pytest.param(9, True, id="9_is_odd"),
    pytest.param(10, False, id="10_is_even"),
    pytest.param(11, True, id="11_is_odd")
    ])
def test_is_odd(num,expected):
    assert (num%2!=0) == expected