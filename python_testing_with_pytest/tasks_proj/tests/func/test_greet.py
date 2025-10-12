import sys

def greet():
    print('Hello real world!')


def test_greet(monkeypatch):
    monkeypatch.setattr(sys.modules[__name__], "greet", lambda: "Hello test!")
    assert greet() == 'Hello test!'


print(greet())

