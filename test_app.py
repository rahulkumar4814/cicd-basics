import pytest

from app import greet


def test_greet():
    assert greet("Rahul") == "Hello, Rahul!"

def test_greet_strips_spaces():
    assert greet("  Asha ") == "Hello, Asha!"

def test_empty_name_is_rejected():
    with pytest.raises(ValueError):
        greet("  ")

def test_shout():
    assert shout("rahul") == "HELLO, RAHUL!"