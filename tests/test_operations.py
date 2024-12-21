from src.math_operations import add,mul

def test_add():
    assert add(2,3) == 5
    assert add(5,4) == 9

def test_mul():
    assert mul(3,4) == 12
    assert mul(5,6) == 30
