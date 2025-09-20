import pytest


@pytest.fixture(params=["Chrome", "Firefox", "Edge", "MyBrowser"])
def browser(request):
    return request.param

def test_browser_launch(browser):
    print(f"Running test on: {browser}")
    assert browser in ["Chrome", "Firefox", "Edge"]


