import mathlib

def test_calc_total():
    total = mathlib.calc_total(5,4)
    assert total == 9



def test_calc_multiply():
     result = mathlib.calc_multipy(10,3)
     assert result == 30