import pytest

@pytest.mark.parametrize("a,b,expected",[
    (2,4,6),
    (1,2,3),
    (3,4,7),
    (4,5,9),
    (5.0,6.0,11.0),
    (6.0,7.0,13.0)
    ])
def test_add(a,b,expected):
    assert a + b == expected