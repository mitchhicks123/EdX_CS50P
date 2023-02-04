from um import count
import pytest


def test_count_space():
    assert count("um") == 1
    assert count(" um    ") == 1


def test_count_word():
    assert count("album") == 0
    assert count("um, the umpire is an rum sucker") == 1


def test_count_case():
    assert count("UM") == 1
    assert count("UM, um, Um....") == 3
