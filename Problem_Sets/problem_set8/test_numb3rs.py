import pytest
from numb3rs import validate


def test_validate_range():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("21.23.7.256") == False


def test_validate_inputs():
    assert validate("cat") == False
    assert validate("a.a.a.a") == False
    assert validate("123.123.123.cat.") == False
    assert validate("-24.6.0.89") == False
    assert validate("99.0.0.2") == True
