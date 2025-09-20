import pytest

def divide(a, b):
    return a/b

def is_even_or_odd(x):
    if x%2 == 0:
        return "EVEN"
    else:
        return "ODD"

@pytest.mark.parametrize("number, expected", [
    (2,"EVEN"),
    (3,"ODD"),
])

def test_even_or_odd(number, expected):
    result = is_even_or_odd(number)
    assert result == expected

@pytest.mark.xfail(reason='Divide by zero is not handled', strict=True)
def test_divide_by_zero():
    assert divide(1, 0) == 0

@pytest.mark.xfail(condition=True, reason="Known bug")
def test_sub_bug():
    result = 5-3
    assert result == 1
