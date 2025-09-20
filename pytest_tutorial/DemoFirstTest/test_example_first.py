import pytest


def is_even_or_odd(n):

    if n%2 == 0:
        return "Even"
    else: 
        return "Odd"


@pytest.mark.smoke
def test_even_number():
    result = is_even_or_odd(4)
    print(f"Test for 4: {result}")


@pytest.mark.regression
def test_odd_number():
    result = is_even_or_odd(7)
    print(f"Test for 7: {result}")


@pytest.mark.skip(reason="Functionality not developed")
def test_large_even_number():
    result = is_even_or_odd(100000000)
    assert result == "Even", "100000000 should be even"

feature_available = False

@pytest.mark.skipif(not feature_available, reason="Feature not available")
def test_large_odd_number():
    result = is_even_or_odd(1000000001)
    assert result == "Odd", "1000000001 should be even"
