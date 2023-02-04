import fuel
import pytest


def test_convert():
    assert fuel.convert("1/3") == 33
    assert fuel.convert("3/4") == 75
    assert fuel.convert("1/1") == 100
    assert fuel.convert("0/3") == 0

    with pytest.raises(ValueError):
        fuel.convert("5/4"),
        fuel.convert("test/test"),
        fuel.convert("t/3")

    with pytest.raises(ZeroDivisionError):
        fuel.convert("5/0"),
        fuel.convert("0/0")


def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(25) == "25%"
