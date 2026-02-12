import  pytest

@pytest.mark.parametrize("num",[1,2,3,4])
def test_is_positive(num):
   assert num > 0
