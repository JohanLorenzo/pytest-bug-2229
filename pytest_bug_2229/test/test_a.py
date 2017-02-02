import pytest

from pytest_bug_2229.a import bar

def test_bar(monkeypatch):
    def foo_patch():
        # In real life, no exception would be thrown
        raise Exception('Victory! foo has been patched')

    monkeypatch.setattr('pytest_bug_2229.b.foo', foo_patch)

    bar()
