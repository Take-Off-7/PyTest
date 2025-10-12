import pytest


def test_pass_fail(testdir):
    """
    Ensure that pytest shows one pass (.) and one failure (F)
    in the short test summary when no plugins modify output.
    """
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """)

    result = testdir.runpytest()

    # result.stdout.fnmatch_lines(['* .F *', '* .F'])  # Expect . for pass, F for fail
    assert '.F' in result.stdout.str()
    assert result.ret == 1


@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """)
    return testdir


def test_with_nice(sample_test):
    result = sample_test.runpytest('--nice')
    # result = sample_test.runpytest("--nice", "-p", "pytest_nice")
    # result.stdout.fnmatch_lines(['*.O'])  # Expect . for pass, O for fail
    assert '.O' in result.stdout.str()
    assert result.ret == 1


def test_with_nice_verbose(sample_test):
    result = sample_test.runpytest('-v', '--nice')
    # result = sample_test.runpytest('-v', '--nice', '-p', 'pytest_nice')
    result.stdout.fnmatch_lines([
        '*test_fail*OPPORTUNITY for improvement*',
    ])
    assert result.ret == 1


def test_not_nice_verbose(sample_test):
    result = sample_test.runpytest('-v')
    # result = sample_test.runpytest('-v', '-p', 'pytest_nice')
    result.stdout.fnmatch_lines([
        '*test_fail*FAILED*',
    ])
    assert result.ret == 1


def test_header(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['Thanks for running the tests, codespace!'
])


def test_header_not_nice(sample_test):
    result = sample_test.runpytest()
    thanks_message = 'Thanks for running the tests.'
    assert thanks_message not in result.stdout.str()


def test_help_message(testdir):
    result = testdir.runpytest('--help')
    result.stdout.fnmatch_lines([
        'Custom options:',
        '*--nice*turn failures into opportunities*',
    ])

def test_nice_ini_setting(testdir):
    testdir.makepyfile(
        """
            def test_dummy():
                assert True         
        """
    )

    result = testdir.runpytest()
    print(result.stdout.str())
    # assert 'OPPORTUNITY for improvement' in result.stdout.str()
