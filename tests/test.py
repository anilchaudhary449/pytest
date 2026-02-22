# test
from unit_testing_classes.unit_testing_classes import Accumulator

def test_accumulator_init():
    acc = Accumulator()
    assert acc.count == 0

def test_accumulator_add_one():
    acc = Accumulator()
    acc.add(1)
    assert acc.count == 1

def test_accumulator_add_two():
    acc = Accumulator()
    acc.add(2)
    assert acc.count == 2
def test_accumulator_add_three():
    acc = Accumulator()
    acc.add(3)
    assert acc.count == 3
def test_accumulator_add_four():
    acc = Accumulator()
    acc.add(4)
    assert acc.count == 4
def test_accumulator_add_five():
    acc = Accumulator()
    acc.add(5)
    assert acc.count == 5
def test_accumulator_add_default():
    acc = Accumulator()
    acc.add()
    assert acc.count == 1

