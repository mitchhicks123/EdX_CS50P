from working import convert
import pytest


def test_convert_hrs():
    assert convert("9 AM to 6 PM") == ("09:00 to 18:00")
    assert convert("12:23 AM to 12:58 PM") == ("00:23 to 12:58")
    assert convert("9:00 PM to 3 AM") == ("21:00 to 03:00")

    with pytest.raises(ValueError):
        convert("0 AM to 9PM")


def test_convert_mins():
    assert convert("9:00 AM to 6 PM") == ("09:00 to 18:00")
    assert convert("12:41 AM to 6 PM") == ("00:41 to 18:00")

    with pytest.raises(ValueError):
        convert("12:60 AM to 9 PM")
