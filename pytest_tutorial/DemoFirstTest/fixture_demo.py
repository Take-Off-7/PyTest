import pytest


@pytest.fixture(scope=)
def setup_environment():
    print("Setting up environment")
    yield "Environment is ready for testing"
    print("Tearing up environment")


def test_example_action(setup_environment):
    print(f"Executing my first test with fixture: {setup_environment}")
    # assert setup_environment == "Environment is ready for testing"
    assert "ready" in setup_environment

