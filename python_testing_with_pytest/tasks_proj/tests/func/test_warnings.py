import warnings
import pytest


def lame_function():
    warnings.warn("Please stop using this", DeprecationWarning)
    # rest of function


def test_lame_function_1(recwarn):
    lame_function()
    assert len(recwarn) == 1
    w = recwarn.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'


def test_lame_function_2():
    with pytest.warns(Warning) as warning_list:
        lame_function()
    assert len(warning_list) == 1
    w = warning_list.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'


def test_lame_function_3():
    with pytest.warns(DeprecationWarning, match="Please stop using this"):
        lame_function()



def divide_by_zero(a, b):
    if b == 0:
        warnings.warn("Cannot divide by zero", UserWarning)
        return None
    return a / b


def test_divide_by_zero_1(recwarn):
    result = divide_by_zero(10, 0)
    assert result is None
    w = recwarn.pop()
    assert issubclass(w.category, UserWarning)
    assert "Cannot divide by zero" in str(w.message)


def test_divide_by_zero_2():
    with pytest.warns(UserWarning, match="Cannot divide by zero"):
        divide_by_zero(10, 0)
