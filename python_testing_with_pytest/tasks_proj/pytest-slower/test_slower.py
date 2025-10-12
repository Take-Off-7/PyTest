import pytest
import time
import random


@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())


def test_fast_slow(testdir):
    # Create a temporary test file
    testdir.makepyfile("""
        import time

        def test_fast():
            assert 1 + 1 == 2

        def test_slow():
            time.sleep(0.1)
            assert True

        def test_slower():
            time.sleep(1.0)
            assert True
    """)

    # First run: all should pass, durations are cached
    result1 = testdir.runpytest()
    assert result1.ret == 0  # Passed

    # Second run: test_slower may exceed 2x previous duration
    result2 = testdir.runpytest("-q")
    print(result2.stdout.str())

