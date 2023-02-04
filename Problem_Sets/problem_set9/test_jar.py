import pytest
from jar import Jar


def test_str():
    cookie = Jar()
    assert str(cookie) == ""
    cookie.deposit(12)
    assert str(cookie) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    cookie.withdraw(6)
    assert str(cookie) == "🍪🍪🍪🍪🍪🍪"


def test_size():
    cookie = Jar()
    assert cookie.size == 0

    cookie.deposit(2)
    assert cookie.size == 2

    cookie.withdraw(1)
    assert cookie.size == 1


def test_deposit():

    cookie = Jar()
    cookie.deposit(2)
    assert cookie.size == 2

    cookie.deposit(2)
    assert cookie.size == 4

    with pytest.raises(ValueError):
        cookie.deposit(18)
